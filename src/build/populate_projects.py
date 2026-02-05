from __future__ import annotations

import argparse
import json
from pathlib import Path
from xml.sax.saxutils import escape


def macro_user_home(p: Path) -> str:
    home = Path.home().resolve()
    p = p.resolve()
    try:
        rel = p.relative_to(home)
        return f"$USER_HOME$/{rel.as_posix()}"
    except ValueError:
        return p.as_posix()


def title_from_name(name: str) -> str:
    # subject_1 -> Subject 1
    return name.replace("_", " ").strip().title()


def xml_attr(v: str) -> str:
    # escape for attribute values
    return escape(v, {'"': "&quot;"})


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--projects-root", required=True)
    args = ap.parse_args()

    manifest_path = Path(args.manifest).expanduser().resolve()
    out_path = Path(args.out).expanduser().resolve()
    projects_root = Path(args.projects_root).expanduser().resolve()

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    sources = manifest.get("practicals", {}).get("sources", [])
    names = [s["name"] for s in sources if isinstance(s, dict) and "name" in s]

    if not names:
        raise SystemExit("No practicals.sources[*].name found in manifest.json")

    entries = []
    for name in reversed(names):
        key = macro_user_home(projects_root / name)
        title = title_from_name(name)
        entries.append(
            "        <entry key=\"{key}\">\n"
            "          <value>\n"
            "            <RecentProjectMetaInfo frameTitle=\"{title}\" opened=\"true\">\n"
            "            </RecentProjectMetaInfo>\n"
            "          </value>\n"
            "        </entry>\n".format(
                key=xml_attr(key),
                title=xml_attr(title),
            )
        )

    xml = (
        "<application>\n"
        "  <component name=\"RecentProjectsManager\">\n"
        "    <option name=\"additionalInfo\">\n"
        "      <map>\n"
        "{entries}"
        "      </map>\n"
        "    </option>\n"
        "  </component>\n"
        "</application>\n"
    ).format(entries="".join(entries))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(xml, encoding="utf-8")

    print(f"Wrote {out_path} with {len(names)} projects.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

