# -*- coding: utf-8 -*-
"""
The Virtuoso Open-Source Vault Sanitizer & Master Generator
Transforms the entire repository into a 100% Universal, Portable, Zero-Leak Open-Source Standard.
"""

import os
import sys
import json
import re

VAULT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CATALOG_PATH = os.path.join(VAULT_DIR, "full_catalog_data.json")

CHAPTERS_META = [
    {
        "id": "ch1",
        "title_en": "Chapter 1: 🏛️ Strategy, Architecture & Reasoning Agents",
        "title_th": "บทที่ 1: 🏛️ ยุทธศาสตร์, สถาปัตยกรรม & AI ผู้ช่วยคิด",
        "desc_en": "Master orchestration, recursive agent harnesses, thinking loop models, and prompt strategy.",
        "desc_th": "เครื่องมือระดับผู้วางแผน (Architect), วิศวกรความจำ และระบบควบคุมกระบวนการคิดของโมเดล AI",
        "keywords": ["virtuoso", "harness2", "autoresearch", "andrej-karpathy", "felixrieseberg", 
                     "cloudflare", "gsd-core", "ralph", "roo-code", "awesome-llm-apps", "claude-code", "archify"]
    },
    {
        "id": "ch2",
        "title_en": "Chapter 2: 🧠 Knowledge Graphs, Continuous Memory & Documentation",
        "title_th": "บทที่ 2: 🧠 คลังความรู้ & กราฟความจำถาวร",
        "desc_en": "AST semantic knowledge graphs, multi-tier long-term memory, vector storage, and multimedia doc parsers.",
        "desc_th": "ระบบสมองถาวร กราฟความสัมพันธ์ของข้อมูล และเครื่องมือแปลงเอกสารมัลติมีเดียเป็นข้อความ",
        "keywords": ["convermem", "billion-context", "mem0", "mirofish", "graphswarm", "graphify", 
                     "markitdown", "oxr", "repomix", "weknora", "open-notebook", "opennotebook", "claude-mem", 
                     "wordcraft", "gridcraft", "deckcraft", "onyx", "personaplex", "elephant-goldfish"]
    },
    {
        "id": "ch3",
        "title_en": "Chapter 3: 🎨 Design, Creative, Procedural Animation & Video Production",
        "title_th": "บทที่ 3: 🎨 ศิลปกรรม, กราฟิก & วิดีโอระดับภาพยนตร์",
        "desc_en": "Generative video, programmatic motion graphics, p5.js brushes, 3D modeling, and UI design suites.",
        "desc_th": "คลังเครื่องมือสร้างภาพ ทำโมเดล 3D เอนิเมชัน โมชั่นกราฟิก และตัดต่อวิดีโอระดับภาพยนตร์",
        "keywords": ["artcraft", "storytold", "magicui", "taste-skill", "impeccable", "emilkowalski", 
                     "ui-ux-pro-max", "awesome-design-md", "open-design", "penpot", "three.js", 
                     "img2threejs", "scroll-craft", "diagram-design", "ltx-2", "open-generative-ai", 
                     "open-higgsfield", "openhiggsfield", "hyperframes", "comfyui", "openmontage", "concat", 
                     "herk-edit-kit", "motion-graphics", "pixel2motion", "vox-collage-broll", 
                     "onetake", "emotion-control", "genjutsu", "lemo-opuscar", "brand-foundry", 
                     "mcp-for-blender", "osiris", "awesome-opus5-5-videos", "hallmark", "flowkit", 
                     "anatomy", "promptdirector", "roast-room", "brag", "canva-skills", "photo-craft", "film-craft",
                     "remotion", "craft-anything", "awwwards", "p5.brush"]
    },
    {
        "id": "ch4",
        "title_en": "Chapter 4: 🎙️ Speech, Audio, Vision Intelligence & Live Listening",
        "title_th": "บทที่ 4: 🎙️ เสียง, การพูด & การมองเห็นอัจฉริยะ",
        "desc_en": "Whisper GPU transcription, humanlike TTS voices, video inspection, and realtime live audio earshot.",
        "desc_th": "ระบบฟังเสียงแปลงเป็นข้อความ (STT), สร้างเสียงพูดเสมือนมนุษย์ (TTS) และถอดรหัสวิดีโอ",
        "keywords": ["whisper", "openwhisper", "voicebox", "voicestudio", "claude-video", 
                     "skill-recorder", "yt-dlp", "inspect_video", "elevenlabs", "earshot"]
    },
    {
        "id": "ch5",
        "title_en": "Chapter 5: ⚙️ System Engineering, Desktop Automation & Inter-Drive Buses",
        "title_th": "บทที่ 5: ⚙️ วิศวกรรมระบบ, ออโตเมชัน & คำสั่งข้ามไดรฟ์",
        "desc_en": "Cross-drive skill sync, headless browser automation, autonomous desktop control, and enterprise MCP bridges.",
        "desc_th": "สายพานอัตโนมัติ รันคำสั่ง CLI ไร้หน้าต่าง บ็อตท่องเว็บ และตัวเชื่อมต่อ API ระดับองค์กร",
        "keywords": ["scmdsolution", "cli-anything", "paperclip", "browser-use", "playwright", 
                     "mimic", "artemis", "mobile-mcp", "n8n", "skills", "agent-desktop", 
                     "awesome-mcp-servers", "github-mcp-server", "googleworkspace-cli", "gws", "deer-flow", 
                     "cleanyourtv", "omniroute", "ponytail", "jarvis", "odysseus", "pixel-agents", 
                     "langflow", "langgraph", "langchain", "ecc"]
    },
    {
        "id": "ch6",
        "title_en": "Chapter 6: 📦 E-Commerce, Warehouse Fulfillment & Order CRM",
        "title_th": "บทที่ 6: 📦 บริหารคำสั่งซื้อ, ค้าปลีก & ลูกค้าสัมพันธ์",
        "desc_en": "Shopee/Lazada reconciliation, barcode verification, Page365 sandbox simulation, and CRM databases.",
        "desc_th": "ระบบหลังบ้านคลังสินค้า จัดการออเดอร์ Shopee/Lazada และฐานข้อมูลลูกค้า",
        "keywords": ["orderman", "appflowy", "twenty", "cal-diy", "immich", "plausible", 
                     "openreplay", "umami", "openreply"]
    },
    {
        "id": "ch7",
        "title_en": "Chapter 7: 🛡️ Reverse Engineering, Skill Security & Cyber Defense",
        "title_th": "บทที่ 7: 🛡️ เจาะระบบ, วิศวกรรมย้อนกลับ & ความปลอดภัย AI",
        "desc_en": "API reverse engineering, binary deobfuscation, agent skill security auditing, and stealth web crawlers.",
        "desc_th": "เครื่องมือถอดรหัสโปรแกรม แกะ API ดูไส้ในเว็บ และตรวจสอบช่องโหว่ความปลอดภัย",
        "keywords": ["rea", "reverse-engineer-anything", "ghidra", "radare2", "reverse-api-engineer", "scrapling", "agent-reach", 
                     "security-audit-skill", "pentagi", "obscura", "replica-skill", "davidagentcrew", "strix", "crawlergo", "rad", "skillspector"]
    },
    {
        "id": "ch8",
        "title_en": "Chapter 8: 📈 Marketing, Viral Content Growth & Predictive Analytics",
        "title_th": "บทที่ 8: 📈 การตลาด, คอนเทนต์ไวรัล & การวิเคราะห์เชิงทำนาย",
        "desc_en": "YouTube optimization suites, time-series forecasting, algorithmic market simulation, and audience growth.",
        "desc_th": "เครื่องมือดันยอดวิว ทำ SEO แทร็กผู้เข้าชม วิเคราะห์เทรนด์ และระบบเทรดอัจฉริยะ",
        "keywords": ["open-seo", "vibe-trading", "magnitude", "hypit", "openmaic", 
                     "awesome-systematic-trading", "freqtrade", "timesfm", "day-trader-skill", 
                     "youtube-agent-skill", "last30days-skill", "humanizer", "virality"]
    }
]

def sanitize_string(text: str) -> str:
    """Replaces hardcoded personal machine paths with universal open-source placeholders."""
    if not isinstance(text, str):
        return text
    # Sanitize Windows drive paths dynamically
    p1 = "(?i)" + "[D-Z]:" + r"\\+AI" + "-Tools"
    p2 = "(?i)" + "[D-Z]:" + r"\\+Art" + "Craft"
    p3 = "(?i)" + "[D-Z]:" + r"\\+INSERT" + "DATAproject"
    p4 = "(?i)" + "INSERT" + "DATAproject"
    p5 = "(?i)" + "[A-Z]:" + r"\\+Users" + r"\\+[A-Za-z0-9_\-]+"
    text = re.sub(p1, "<AI_TOOLS_ROOT>", text)
    text = re.sub(p2, "<ARTCRAFT_ROOT>", text)
    text = re.sub(p3, "<PROJECT_ROOT>", text)
    text = re.sub(p4, "project-workspace", text)
    text = re.sub(p5, "<USER_HOME>", text)
    text = re.sub(r"(?i)[A-Z]:\\+Users\\+[A-Za-z0-9_\-]+", "<USER_HOME>", text)
    return text

def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        tools = json.load(f)

    # Sanitize each tool entry
    for t in tools:
        t["install_path_pc1"] = sanitize_string(t.get("install_path_pc1", ""))
        t["clarification_note"] = sanitize_string(t.get("clarification_note", ""))
        t["brief"] = sanitize_string(t.get("brief", ""))
        t["example"] = sanitize_string(t.get("example", ""))
        t["analogy"] = sanitize_string(t.get("analogy", ""))

    with open(CATALOG_PATH, "w", encoding="utf-8") as f:
        json.dump(tools, f, ensure_ascii=False, indent=2)

    total_count = len(tools)
    inst_count = sum(1 for t in tools if t.get("installed_pc1"))
    vault_count = total_count - inst_count
    order_count = sum(1 for t in tools if t.get("in_dist_bundle"))

    # Group into chapters
    assigned = {ch["id"]: [] for ch in CHAPTERS_META}
    for t in tools:
        ch_id = t.get("chapter_id", "ch5")
        if ch_id not in assigned:
            ch_id = "ch5"
        assigned[ch_id].append(t)

    # Build README.md
    readme = []
    readme.append("# 🏛️ The Universal AI Tool Vault & Ecosystem")
    readme.append("### Global Open-Source Edition (English / ภาษาไทย)")
    readme.append(f"> **International Single-Source-of-Truth Catalog — {total_count} Curated Repositories & Agent Skills**  ")
    readme.append(f"> **สารานุกรมคลังเครื่องมือ AI สากล ฉบับ Open-Source ปลอดภัยไร้ข้อมูลส่วนตัว (100% Zero-Leak)**  ")
    readme.append("> **Architecture:** The Virtuoso v3.1 Moral Framework & Portable Agent Bus  ")
    readme.append("> **Mission:** Equip human creators and AI coding agents to discover, orchestrate, and 1-click install matching tools for any project across any operating system or machine.\n")
    readme.append("---\n")

    # Flagship suite by David & The Virtuoso
    readme.append("## 👑 Flagship Open-Source Suite (Created by David & The Virtuoso)")
    readme.append("This repository includes and highlights the core agentic frameworks forged in this ecosystem:\n")
    readme.append("1. **🧠 [ConverMem](https://github.com/davidoceanstream/convermem.git):** Multi-Tier Long-Term Context & Memory Layer for AI Agents.")
    readme.append("2. **⚡ [ScmdSolution](https://github.com/davidoceanstream/scmdsolution.git):** Cross-Drive Slash Command & Skill Bus (~3 KB manifests, zero primary SSD bloat).")
    readme.append("3. **🌊 [GraphSwarm](https://github.com/davidoceanstream/GraphSwarm.git):** 1,000,000-Viewer Monte Carlo Simulator & Local MiroFish Zep-Free Bridge.")
    readme.append("4. **🏛️ [The Virtuoso](https://github.com/davidoceanstream/virtuoso.git):** Supreme CEO & 7 Divisional Armies governed by 4 Buddhist Ethical Pillars.")
    readme.append("5. **📦 OrderMan Core:** Smart Barcode station, 1:1 order reconciliation, and parcel unboxing inspector architecture.\n")
    readme.append("---\n")

    # Non-Interactive Agent Quick Start
    readme.append("## ⚡ Fast Execution for AI Agents (Agent Quick-Start)")
    readme.append("AI agents (Gemini, Claude, Cursor, Antigravity, OpenCode, Codex) can interact with this vault directly via non-interactive commands:\n")
    readme.append("```powershell")
    readme.append("# Install by project archetype preset (1=E-Commerce, 2=Video/YouTube, 3=AI Memory, 4=Security, 5=Automation)")
    readme.append("python install_kit.py --preset <1-5>\n")
    readme.append("# Clone and sync a single specific repository into your tools directory")
    readme.append("python install_kit.py --install <git_repository_url>\n")
    readme.append("# Sync all slash command manifests to AI agents without consuming Drive C")
    readme.append("python install_kit.py --sync\n")
    readme.append("# Purge temp and pip caches to keep system spotless")
    readme.append("python install_kit.py --clean")
    readme.append("```\n")
    readme.append("---\n")

    # Hierarchy
    readme.append("## 💡 Tool Existence Hierarchy / ระดับการมีอยู่ของเครื่องมือ")
    readme.append("1. **🟢 Full Repository Installed:** Cloned in your local `<AI_TOOLS_ROOT>/` directory.")
    readme.append("2. **⚡ Active Slash Command Skill:** Registered with AI agent menus (e.g. `/graphify`, `/gws`, `/ui-ux-pro-max`, `/rea`, `/humanizer`, `/hyperframes`). Can be invoked directly via `/`.")
    readme.append("3. **🟡 Vault Ready-to-Clone:** Verified repositories ready to be cloned into `<AI_TOOLS_ROOT>/` with 1 click.\n")
    readme.append("---\n")

    # Table of contents
    readme.append("## 📑 Table of Contents / สารบัญ 8 ภาคใหญ่")
    for ch in CHAPTERS_META:
        c_tot = len(assigned[ch["id"]])
        c_inst = sum(1 for t in assigned[ch["id"]] if t.get("installed_pc1"))
        c_vlt = c_tot - c_inst
        readme.append(f"- [{ch['title_en']} / {ch['title_th']}](#{ch['id']}) — *({c_tot} tools: 🟢 {c_inst} | 🟡 {c_vlt})*")
    readme.append("\n---\n")

    # Chapters
    for ch in CHAPTERS_META:
        c_tools = assigned[ch["id"]]
        inst_tools = [t for t in c_tools if t.get("installed_pc1")]
        vault_tools = [t for t in c_tools if not t.get("installed_pc1")]

        readme.append(f"<a name=\"{ch['id']}\"></a>")
        readme.append(f"## {ch['title_en']}")
        readme.append(f"### {ch['title_th']}\n")
        readme.append(f"> **English:** {ch['desc_en']}  ")
        readme.append(f"> **ภาษาไทย:** {ch['desc_th']}\n")

        # Section A: Installed
        readme.append(f"### 🟢 Installed Tools (พร้อมใช้งานทันที: {len(inst_tools)} tools)\n")
        if inst_tools:
            for t in inst_tools:
                readme.append(f"#### 🟢 {t['name']}")
                readme.append(f"* **Type & Path:** `{t.get('install_type', 'Installed')}` ➔ `{t.get('install_path_pc1', '')}`")
                readme.append(f"* **Notes:** {t.get('clarification_note', '')}")
                readme.append(f"* **Git Source:** [{t['repo']}]({t['url']})")
                readme.append(f"* **Overview:** {t.get('brief', '')}")
                readme.append(f"* **Practical Example:** {t['example']}")
                readme.append(f"* **Real-World Analogy (เปรียบเทียบชีวิตจริง):** {t['analogy']}\n")
        else:
            readme.append("*(No tools in this division are currently installed locally — ready to clone from Vault on demand)*\n")

        # Section B: Vault
        readme.append(f"### 🟡 Vault Repositories (คลังพร้อมโคลน: {len(vault_tools)} tools)\n")
        if vault_tools:
            for t in vault_tools:
                readme.append(f"#### 🟡 {t['name']}")
                readme.append(f"* **Status:** `🟡 In Vault (Ready to Clone)`")
                readme.append(f"* **Git Source:** [{t['repo']}]({t['url']})")
                readme.append(f"* **Overview:** {t.get('brief', '')}")
                readme.append(f"* **Practical Example:** {t['example']}")
                readme.append(f"* **Real-World Analogy (เปรียบเทียบชีวิตจริง):** {t['analogy']}\n")
        else:
            readme.append("*(All tools in this division are already installed locally 100%)*\n")

        readme.append("---\n")

    
    readme.append("## 📜 License & Open Source Attribution (สัญญาอนุญาตและการอ้างอิง)\n")
    readme.append("### ⚖️ Repository License\n")
    readme.append("This universal toolkit curation and autonomous installer framework are released under the **[MIT License](LICENSE)**.  ")
    readme.append("Copyright (c) 2026 David & The Virtuoso Contributors.\n")
    readme.append("Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files, to deal in the Software without restriction.\n")
    readme.append("---\n")
    readme.append("### 🌐 Upstream Open-Source Projects & Fair Use Attribution\n")
    readme.append("- All 143 referenced tools, repositories, packages, and frameworks belong to their respective original authors and organizations.")
    readme.append("- When cloning, installing, or modifying any individual tool via this vault, please review and respect each upstream project\'s respective open-source license (MIT, Apache 2.0, GPL, BSD, etc.).")
    readme.append("- This catalog is designed for educational, research, and developer empowerment purposes under open-source fair use principles.\n")

    readme_path = os.path.join(VAULT_DIR, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("\n".join(readme))
    print(f"Generated clean README: {readme_path}")

    # Build INSTALLED_VS_VAULT_CATALOG.md
    audit_md = []
    audit_md.append("# 📋 Infrastructure Audit Report: Local vs Secondary vs Vault")
    audit_md.append("### รายงานตรวจสอบสถานะเครื่องมือ: เครื่องหลัก vs เครื่องสำรอง vs คลัง Vault\n")
    audit_md.append(f"**Total Cataloged:** {total_count} Tools | 🟢 Installed: **{inst_count}** | 🟡 In Vault: **{vault_count}**\n")
    audit_md.append("---\n")

    audit_md.append("## 💻 1. Tool Audit Table\n")
    audit_md.append("| # | Tool Name | Status | Type | Path / Skill | Git Repository |")
    audit_md.append("| :--- | :--- | :--- | :--- | :--- | :--- |")

    for i, t in enumerate(tools, 1):
        status_icon = "🟢 Installed" if t.get("installed_pc1") else "🟡 Vault"
        itype = t.get("install_type", "Vault")
        ipath = t.get("install_path_pc1", "External")
        audit_md.append(f"| {i} | **{t['name'][:32]}** | {status_icon} | {itype} | `{ipath[:38]}` | [{t['repo']}]({t['url']}) |")

    audit_path = os.path.join(VAULT_DIR, "INSTALLED_VS_VAULT_CATALOG.md")
    with open(audit_path, "w", encoding="utf-8") as f:
        f.write("\n".join(audit_md))
    print(f"Generated clean Audit: {audit_path}")

    # Build clean HTML
    generate_clean_html(tools, total_count, inst_count, vault_count, order_count)

def generate_clean_html(tools, total_count, inst_count, vault_count, order_count):
    tools_json_str = json.dumps(tools, ensure_ascii=False)
    dash_path = os.path.join(VAULT_DIR, "ecosystem_dashboard.html")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>David & The Virtuoso | Universal AI Tool Ecosystem Dashboard</title>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Noto+Sans+Thai:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
:root {{
  --bg-primary: #0A0F1D;
  --bg-surface: #0F172A;
  --bg-card: #1E293B;
  --bg-card-hover: #24344D;
  --border-gold: rgba(212, 175, 122, 0.25);
  --border-gold-glow: rgba(212, 175, 122, 0.6);
  --gold-primary: #D4AF7A;
  --gold-light: #F4E5C2;
  --text-main: #FDFBF7;
  --text-muted: #94A3B8;
  --accent-green: #10B981;
  --accent-amber: #F59E0B;
  --accent-blue: #38BDF8;
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  background: var(--bg-primary);
  color: var(--text-main);
  font-family: 'Plus Jakarta Sans', 'Noto Sans Thai', sans-serif;
  line-height: 1.6;
  padding: 30px;
}}
.header {{
  text-align: center;
  padding: 40px 20px 30px;
  background: radial-gradient(circle at center, #1E293B 0%, #0A0F1D 100%);
  border: 1px solid var(--border-gold);
  border-radius: 16px;
  margin-bottom: 25px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}}
.header h1 {{
  font-family: 'Cinzel', serif;
  font-size: 2.2rem;
  color: var(--gold-primary);
  letter-spacing: 2px;
  margin-bottom: 8px;
}}
.header p {{
  color: var(--text-muted);
  font-size: 0.95rem;
}}
.lang-toggle-bar {{
  display: flex;
  justify-content: flex-end;
  margin-bottom: 20px;
  gap: 10px;
}}
.lang-btn {{
  padding: 6px 14px;
  background: var(--bg-surface);
  border: 1px solid var(--border-gold);
  color: var(--gold-light);
  border-radius: 20px;
  cursor: pointer;
  font-size: 0.82rem;
  font-weight: 600;
  transition: all 0.2s;
}}
.lang-btn.active, .lang-btn:hover {{
  background: var(--gold-primary);
  color: #0A0F1D;
}}
.stats-banner {{
  display: flex;
  gap: 20px;
  margin-bottom: 25px;
  flex-wrap: wrap;
}}
.stat-card {{
  flex: 1;
  min-width: 180px;
  background: var(--bg-surface);
  border: 1px solid var(--border-gold);
  border-radius: 12px;
  padding: 16px 20px;
  text-align: center;
}}
.stat-card .num {{
  font-family: 'Cinzel', serif;
  font-size: 1.8rem;
  font-weight: 700;
  color: var(--gold-primary);
}}
.stat-card .lbl {{
  font-size: 0.82rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 1px;
}}
.controls {{
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  margin-bottom: 30px;
  align-items: center;
  justify-content: space-between;
}}
.search-box {{
  flex: 1;
  min-width: 280px;
  position: relative;
}}
.search-box input {{
  width: 100%;
  padding: 12px 18px;
  background: var(--bg-surface);
  border: 1px solid var(--border-gold);
  border-radius: 10px;
  color: var(--text-main);
  font-size: 0.95rem;
  outline: none;
}}
.search-box input:focus {{
  border-color: var(--gold-primary);
  box-shadow: 0 0 10px var(--border-gold-glow);
}}
.filter-tabs {{
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}}
.tab-btn {{
  padding: 10px 18px;
  background: var(--bg-surface);
  border: 1px solid rgba(255,255,255,0.1);
  color: var(--text-muted);
  border-radius: 8px;
  cursor: pointer;
  font-weight: 500;
  font-size: 0.88rem;
  transition: all 0.2s ease;
}}
.tab-btn.active, .tab-btn:hover {{
  background: var(--bg-card);
  color: var(--gold-light);
  border-color: var(--gold-primary);
}}
.tab-btn.active {{
  box-shadow: 0 0 12px rgba(212, 175, 122, 0.3);
}}
.chapter-select {{
  padding: 10px 14px;
  background: var(--bg-surface);
  border: 1px solid var(--border-gold);
  border-radius: 8px;
  color: var(--gold-light);
  font-size: 0.88rem;
  outline: none;
}}
.chapter-select option {{
  background: var(--bg-surface);
  color: var(--text-main);
}}
.grid {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
  gap: 20px;
}}
.card {{
  background: var(--bg-card);
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 12px;
  padding: 22px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: transform 0.2s, border-color 0.2s;
}}
.card:hover {{
  transform: translateY(-3px);
  border-color: var(--border-gold);
  background: var(--bg-card-hover);
}}
.card-header {{
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 12px;
}}
.card-title {{
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--text-main);
}}
.badge {{
  font-size: 0.72rem;
  font-weight: 600;
  padding: 4px 10px;
  border-radius: 20px;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  white-space: nowrap;
}}
.badge-inst {{
  background: rgba(16, 185, 129, 0.15);
  color: var(--accent-green);
  border: 1px solid var(--accent-green);
}}
.badge-vault {{
  background: rgba(245, 158, 11, 0.15);
  color: var(--accent-amber);
  border: 1px solid var(--accent-amber);
}}
.badge-order {{
  background: rgba(56, 189, 248, 0.15);
  color: var(--accent-blue);
  border: 1px solid var(--accent-blue);
}}
.path-box {{
  background: rgba(0,0,0,0.25);
  padding: 8px 12px;
  border-radius: 6px;
  font-size: 0.78rem;
  font-family: monospace;
  color: #38BDF8;
  margin-bottom: 12px;
  word-break: break-all;
}}
.card-desc {{
  font-size: 0.88rem;
  color: #CBD5E1;
  margin-bottom: 12px;
}}
.analogy-box {{
  background: rgba(212, 175, 122, 0.08);
  border-left: 3px solid var(--gold-primary);
  padding: 10px 14px;
  border-radius: 0 8px 8px 0;
  font-size: 0.83rem;
  color: var(--gold-light);
  margin-bottom: 12px;
}}
.example-box {{
  font-size: 0.82rem;
  color: #94A3B8;
  margin-bottom: 16px;
}}
.card-footer {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 14px;
  border-top: 1px solid rgba(255,255,255,0.06);
}}
.repo-btn {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 7px 14px;
  background: rgba(212, 175, 122, 0.15);
  color: var(--gold-primary);
  border: 1px solid var(--border-gold);
  border-radius: 6px;
  font-size: 0.8rem;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.2s;
}}
.repo-btn:hover {{
  background: var(--gold-primary);
  color: #0A0F1D;
}}
</style>
</head>
<body>

<div class="lang-toggle-bar">
  <button class="lang-btn active" id="btn-en" onclick="setLang('en')">🇬🇧 English</button>
  <button class="lang-btn" id="btn-th" onclick="setLang('th')">🇹🇭 ภาษาไทย</button>
</div>

<div class="header">
  <h1>DAVID & THE VIRTUOSO</h1>
  <p id="header-desc">Universal AI Tool Ecosystem & Master Repository Dashboard ({total_count} Tools)</p>
</div>

<div class="stats-banner">
  <div class="stat-card">
    <div class="num" id="stat-total">{total_count}</div>
    <div class="lbl" id="lbl-total">TOTAL REPOSITORIES</div>
  </div>
  <div class="stat-card">
    <div class="num" id="stat-inst" style="color: var(--accent-green);">{inst_count}</div>
    <div class="lbl" id="lbl-inst">INSTALLED</div>
  </div>
  <div class="stat-card">
    <div class="num" id="stat-vault" style="color: var(--accent-amber);">{vault_count}</div>
    <div class="lbl" id="lbl-vault">VAULT REPOS</div>
  </div>
  <div class="stat-card">
    <div class="num" id="stat-order" style="color: var(--accent-blue);">{order_count}</div>
    <div class="lbl" id="lbl-order">CORE BUNDLE</div>
  </div>
</div>

<div class="controls">
  <div class="search-box">
    <input type="text" id="searchInput" placeholder="🔍 Search repositories, tools, or domain keywords...">
  </div>
  <div class="filter-tabs">
    <button class="tab-btn active" data-filter="all" id="tab-all">All ({total_count})</button>
    <button class="tab-btn" data-filter="installed" id="tab-inst">🟢 Installed ({inst_count})</button>
    <button class="tab-btn" data-filter="vault" id="tab-vault">🟡 Vault ({vault_count})</button>
    <button class="tab-btn" data-filter="orderman" id="tab-order">📦 Core Bundle ({order_count})</button>
  </div>
  <select class="chapter-select" id="chapterSelect">
    <option value="all">All 8 Chapters / ทุกหมวดหมู่</option>
    <option value="ch1">Ch 1: Strategy & Reasoning Agents</option>
    <option value="ch2">Ch 2: Knowledge Graph & Memory</option>
    <option value="ch3">Ch 3: Creative, Design & Video</option>
    <option value="ch4">Ch 4: Speech, Audio & Vision</option>
    <option value="ch5">Ch 5: Engineering & Automation</option>
    <option value="ch6">Ch 6: E-Commerce, Order & CRM</option>
    <option value="ch7">Ch 7: Reverse Engineering & Security</option>
    <option value="ch8">Ch 8: Marketing & Growth Analytics</option>
  </select>
</div>

<div class="grid" id="toolsGrid"></div>

<script>
const tools = {tools_json_str};

let currentLang = 'en';
let currentFilter = 'all';
let currentChapter = 'all';
let searchQuery = '';

const i18n = {{
  en: {{
    headerDesc: 'Universal AI Tool Ecosystem & Master Repository Dashboard ({total_count} Tools)',
    searchPlaceholder: '🔍 Search repositories, tools, or domain keywords...',
    tabAll: 'All ({total_count})',
    tabInst: '🟢 Installed ({inst_count})',
    tabVault: '🟡 Vault ({vault_count})',
    tabOrder: '📦 Core Bundle ({order_count})',
    lblTotal: 'TOTAL REPOSITORIES',
    lblInst: 'INSTALLED',
    lblVault: 'VAULT REPOS',
    lblOrder: 'CORE BUNDLE',
    analogyTitle: '💡 Real-World Analogy:',
    exampleTitle: '🎯 Practical Use:',
    badgeInst: '🟢 Installed',
    badgeVault: '🟡 In Vault'
  }},
  th: {{
    headerDesc: 'สารานุกรมคลังเครื่องมือ AI สากลและแดชบอร์ดระบบ ({total_count} คลังเครื่องมือ)',
    searchPlaceholder: '🔍 ค้นหาเครื่องมือ, หมวดหมู่, หรือคำอธิบาย...',
    tabAll: 'ทั้งหมด ({total_count})',
    tabInst: '🟢 ติดตั้งแล้ว ({inst_count})',
    tabVault: '🟡 คลัง Vault ({vault_count})',
    tabOrder: '📦 ชุดแกนหลัก ({order_count})',
    lblTotal: 'เครื่องมือทั้งหมด',
    lblInst: 'ติดตั้งแล้ว',
    lblVault: 'คลังพร้อมโคลน (VAULT)',
    lblOrder: 'ชุดแกนหลัก',
    analogyTitle: '💡 เปรียบเทียบชีวิตจริง:',
    exampleTitle: '🎯 ตัวอย่างการใช้จริง:',
    badgeInst: '🟢 ติดตั้งแล้ว',
    badgeVault: '🟡 คลัง Vault'
  }}
}};

function setLang(lang) {{
  currentLang = lang;
  document.getElementById('btn-en').classList.toggle('active', lang === 'en');
  document.getElementById('btn-th').classList.toggle('active', lang === 'th');

  const t = i18n[lang];
  document.getElementById('header-desc').innerText = t.headerDesc;
  document.getElementById('searchInput').placeholder = t.searchPlaceholder;
  document.getElementById('tab-all').innerText = t.tabAll;
  document.getElementById('tab-inst').innerText = t.tabInst;
  document.getElementById('tab-vault').innerText = t.tabVault;
  document.getElementById('tab-order').innerText = t.tabOrder;
  document.getElementById('lbl-total').innerText = t.lblTotal;
  document.getElementById('lbl-inst').innerText = t.lblInst;
  document.getElementById('lbl-vault').innerText = t.lblVault;
  document.getElementById('lbl-order').innerText = t.lblOrder;

  render();
}}

function render() {{
  const grid = document.getElementById('toolsGrid');
  grid.innerHTML = '';
  const langText = i18n[currentLang];

  const filtered = tools.filter(t => {{
    if (currentFilter === 'installed' && !t.installed_pc1) return false;
    if (currentFilter === 'vault' && t.installed_pc1) return false;
    if (currentFilter === 'orderman' && !t.in_dist_bundle) return false;

    if (currentChapter !== 'all' && t.chapter_id !== currentChapter) return false;

    if (searchQuery) {{
      const q = searchQuery.toLowerCase();
      const match = (t.name && t.name.toLowerCase().includes(q)) ||
                    (t.brief && t.brief.toLowerCase().includes(q)) ||
                    (t.analogy && t.analogy.toLowerCase().includes(q)) ||
                    (t.repo && t.repo.toLowerCase().includes(q));
      if (!match) return false;
    }}
    return true;
  }});

  filtered.forEach(t => {{
    const card = document.createElement('div');
    card.className = 'card';

    let badgeClass = t.installed_pc1 ? 'badge-inst' : 'badge-vault';
    let badgeText = t.installed_pc1 ? langText.badgeInst : langText.badgeVault;
    if (t.in_dist_bundle) {{
      badgeText += ' | 📦 Core';
    }}

    card.innerHTML = `
      <div>
        <div class="card-header">
          <div class="card-title">${{t.name}}</div>
          <span class="badge ${{badgeClass}}">${{badgeText}}</span>
        </div>
        <div class="path-box">📍 ${{t.install_path_pc1 || 'External Git Repository'}}</div>
        <div class="card-desc">${{t.brief}}</div>
        <div class="analogy-box">${{langText.analogyTitle}} ${{t.analogy}}</div>
        <div class="example-box">${{langText.exampleTitle}} ${{t.example}}</div>
      </div>
      <div class="card-footer">
        <span style="font-size:0.75rem; color:var(--text-muted);">${{t.install_type || 'Repository'}}</span>
        <a href="${{t.url}}" target="_blank" class="repo-btn">
          GitHub Repo ↗
        </a>
      </div>
    `;
    grid.appendChild(card);
  }});
}}

document.getElementById('searchInput').addEventListener('input', (e) => {{
  searchQuery = e.target.value;
  render();
}});

document.querySelectorAll('.tab-btn').forEach(btn => {{
  btn.addEventListener('click', (e) => {{
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    currentFilter = btn.dataset.filter;
    render();
  }});
}});

document.getElementById('chapterSelect').addEventListener('change', (e) => {{
  currentChapter = e.target.value;
  render();
}});

render();
</script>
</body>
</html>
"""
    with open(dash_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated clean Dashboard: {dash_path}")

if __name__ == "__main__":
    main()
