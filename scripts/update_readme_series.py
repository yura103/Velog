import os
import re
import json
from datetime import datetime, timezone
from collections import defaultdict

import requests

GQL_ENDPOINT = "https://v2.velog.io/graphql"
MAX_VISIBLE_PER_SERIES = 5

START_MARK = "<!-- VELOG_SERIES_INDEX:START -->"
END_MARK = "<!-- VELOG_SERIES_INDEX:END -->"

def gql(payload: dict):
    r = requests.post(GQL_ENDPOINT, json=payload, headers={"Content-Type":"application/json"}, timeout=30)
    r.raise_for_status()
    data = r.json()
    if "errors" in data:
        raise RuntimeError(data["errors"])
    return data["data"]

def iso_dt(s: str):
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z","+00:00")).astimezone(timezone.utc)
    except Exception:
        return None

def fetch_series_list(username: str):
    payload = {
        "operationName": "UserSeriesList",
        "variables": {"username": username},
        "query": (
            "query UserSeriesList($username: String!) {"
            "  user(username: $username) {"
            "    series_list { name url_slug posts_count updated_at }"
            "  }"
            "}"
        )
    }
    data = gql(payload)
    user = data.get("user") or {}
    return user.get("series_list") or []

def fetch_all_posts(username: str, limit: int = 50):
    posts = []
    cursor = None
    while True:
        payload = {
            "operationName": "Posts",
            "variables": {"username": username, "cursor": cursor, "limit": limit},
            "query": (
                "query Posts($cursor: ID, $username: String, $temp_only: Boolean, $tag: String, $limit: Int) {"
                "  posts(cursor: $cursor, username: $username, temp_only: $temp_only, tag: $tag, limit: $limit) {"
                "    id title url_slug released_at"
                "  }"
                "}"
            )
        }
        data = gql(payload)
        page = data.get("posts") or []
        if not page:
            break
        posts.extend(page)
        cursor = page[-1]["id"]
        if len(page) < limit:
            break
    return posts

def read_post_series(username: str, url_slug: str):
    payload = {
        "operationName": "ReadPost",
        "variables": {"username": username, "url_slug": url_slug},
        "query": (
            "query ReadPost($username: String, $url_slug: String) {"
            "  post(username: $username, url_slug: $url_slug) {"
            "    series { name url_slug }"
            "  }"
            "}"
        )
    }
    data = gql(payload)
    post = data.get("post")
    if not post:
        return None
    return post.get("series")

def replace_block(readme: str, block: str):
    pattern = re.compile(re.escape(START_MARK) + r".*?" + re.escape(END_MARK), re.DOTALL)
    replacement = f"{START_MARK}\n{block}\n{END_MARK}"
    if pattern.search(readme):
        return pattern.sub(replacement, readme)
    return readme.rstrip() + "\n\n" + replacement + "\n"

def build_block(username: str, series_list: list, posts: list, series_by_post: dict):
    # 그룹핑
    grouped = defaultdict(list)
    no_series = []

    for p in posts:
        slug = p["url_slug"]
        title = p["title"]
        dt = iso_dt(p.get("released_at",""))
        link = f"https://velog.io/@{username}/{slug}"

        item = {"title": title, "link": link, "dt": dt or datetime(1970,1,1,tzinfo=timezone.utc)}

        s = series_by_post.get(slug)
        if s and s.get("url_slug"):
            grouped[s["url_slug"]].append(item)
        else:
            no_series.append(item)

    # 최신순 정렬
    for k in list(grouped.keys()):
        grouped[k].sort(key=lambda x: x["dt"], reverse=True)
    no_series.sort(key=lambda x: x["dt"], reverse=True)

    # 시리즈 표시 이름
    name_by_slug = {s["url_slug"]: s["name"] for s in series_list if s.get("url_slug")}
    ordered = [s["url_slug"] for s in series_list if s.get("url_slug")]
    for k in grouped.keys():
        if k not in ordered:
            ordered.append(k)

    lines = []
    lines.append("## Velog 목차 (시리즈별)")
    lines.append("")
    lines.append("> 자동 생성됨 (시리즈별 최신 글부터).")
    lines.append("")

    def render_section(title, items, series_slug=None):
        lines.append(f"### {title}")
        if series_slug:
            lines.append(f"- 시리즈 링크: https://velog.io/@{username}/series/{series_slug}")
        lines.append("")

        head = items[:MAX_VISIBLE_PER_SERIES]
        tail = items[MAX_VISIBLE_PER_SERIES:]

        for it in head:
            lines.append(f"- [{it['title']}]({it['link']})")

        if tail:
            lines.append("")
            lines.append("<details>")
            lines.append("<summary>더보기</summary>")
            lines.append("")
            for it in tail:
                lines.append(f"- [{it['title']}]({it['link']})")
            lines.append("")
            lines.append("</details>")
        lines.append("")

    for series_slug in ordered:
        items = grouped.get(series_slug)
        if not items:
            continue
        render_section(name_by_slug.get(series_slug, series_slug), items, series_slug)

    if no_series:
        render_section("시리즈 없음", no_series, None)

    return "\n".join(lines).rstrip()

def main():
    username = os.environ.get("VELOG_USERNAME")
    if not username:
        raise RuntimeError("VELOG_USERNAME 환경변수가 필요해요.")

    # ReadPost는 느릴 수 있어서 캐시
    cache_file = ".velog_series_cache.json"
    cache = {}
    if os.path.exists(cache_file):
        with open(cache_file, "r", encoding="utf-8") as f:
            cache = json.load(f)

    series_list = fetch_series_list(username)
    posts = fetch_all_posts(username)

    series_by_post = {}
    changed_cache = False
    for p in posts:
        slug = p["url_slug"]
        if slug in cache:
            series_by_post[slug] = cache[slug]
            continue
        s = read_post_series(username, slug)
        cache[slug] = {"name": s.get("name"), "url_slug": s.get("url_slug")} if s else None
        series_by_post[slug] = cache[slug]
        changed_cache = True

    if changed_cache:
        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(cache, f, ensure_ascii=False, indent=2)

    if not os.path.exists("README.md"):
        with open("README.md", "w", encoding="utf-8") as f:
            f.write("# Velog Archive\n\n")

    with open("README.md", "r", encoding="utf-8") as f:
        readme = f.read()

    block = build_block(username, series_list, posts, series_by_post)
    new_readme = replace_block(readme, block)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_readme)

    print("✅ README 시리즈 목차 갱신 완료")

if __name__ == "__main__":
    main()
