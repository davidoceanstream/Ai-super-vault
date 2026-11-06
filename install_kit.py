# -*- coding: utf-8 -*-
"""
Turnkey AI Tool Installer & Kit Selector (Bilingual: English & Thai)
Supports both Interactive Menu and Non-Interactive CLI Arguments for AI Agents.

Usage by AI Agents or Terminal:
  python install_kit.py --preset 1        # Install Preset 1 directly
  python install_kit.py --preset 2        # Install Preset 2 directly
  python install_kit.py --install <url>   # Clone & sync a specific tool
  python install_kit.py --sync            # Sync slash commands via /scmdsolution
  python install_kit.py --clean           # Purge temp cache via Virtuoso
  python install_kit.py                   # Launch interactive bilingual menu
"""

import os
import sys
import json
import subprocess
import argparse

DEFAULT_ROOT = os.environ.get("AI_TOOLS_ROOT", os.environ.get("AI_TOOLS_DIR", os.path.join(os.path.expanduser("~"), "ai-tools")))
if not os.environ.get("AI_TOOLS_ROOT") and os.path.exists("D:" + os.sep + "AI-Tools"):
    DEFAULT_ROOT = "D:" + os.sep + "AI-Tools"
TOOLS_DIR = DEFAULT_ROOT
CATALOG_PATH = os.path.join(os.path.dirname(__file__), "full_catalog_data.json")

PRESETS = {
    "1": {
        "title_en": "📦 E-Commerce, Order Management & Warehouse Ops (OrderMan Profile)",
        "title_th": "📦 E-Commerce, จัดการออเดอร์ & ระบบหลังบ้าน (OrderMan Profile)",
        "desc_en": "Warehouse fulfillment, barcode station, waybill parsing, video unpacking verification",
        "desc_th": "ระบบหลังบ้านคลังสินค้า, วิเคราะห์คำสั่งซื้อ, สแกนบาร์โค้ด, ตรวจสอบวิดีโอแกะพัสดุ",
        "repos": [
            "https://github.com/davidoceanstream/convermem.git",
            "https://github.com/davidoceanstream/scmdsolution.git"
        ],
        "pip": ["openai-whisper", "playwright", "markitdown", "opencv-python", "fastapi"]
    },
    "2": {
        "title_en": "🎬 Video, YouTube Creator & Creative Media Production",
        "title_th": "🎬 Video, YouTube Creator & ครีเอทีฟมัลติมีเดีย",
        "desc_en": "11 YouTube Agent Skills (/yt-*), 21 hook formulas, retention drop-off analysis, Remotion, p5.brush, Earshot",
        "desc_th": "11 สกิลทำช่อง YouTube, วิเคราะห์กราฟ Retention, เขียนบท 21 Hook, Remotion, p5.brush, Earshot",
        "repos": [
            "https://github.com/Jakeschincariol/youtube-agent-skill.git",
            "https://github.com/remotion-dev/skills.git",
            "https://github.com/acamposuribe/p5.brush.git",
            "https://github.com/Leonxlnx/earshot.git",
            "https://github.com/sirioberati/Genjustsu-Open-Source-Workflow.git"
        ],
        "pip": ["openai-whisper", "yt-dlp"]
    },
    "3": {
        "title_en": "🧠 AI Memory, Knowledge Graph & Multi-Agent Swarm",
        "title_th": "🧠 AI Memory, กราฟความรู้ & จำลองพฤติกรรม Swarm",
        "desc_en": "Continuous context, multi-tier memory, 1,000,000-viewer simulation, local knowledge graphs",
        "desc_th": "ระบบความจำถาวร, กราฟความสัมพันธ์, จำลองพฤติกรรมผู้ชม 1 ล้านคน, สรุปประวัติงาน",
        "repos": [
            "https://github.com/davidoceanstream/convermem.git",
            "https://github.com/mem0ai/mem0.git",
            "https://github.com/lfnovo/open-notebook.git",
            "https://github.com/NVIDIA/personaplex.git",
            "https://github.com/google/elephant-goldfish-model.git"
        ],
        "pip": ["networkx", "numpy"]
    },
    "4": {
        "title_en": "🛡️ Reverse Engineering, API Inspection & Cybersecurity",
        "title_th": "🛡️ เจาะระบบ, วิศวกรรมย้อนกลับ & ความปลอดภัย AI",
        "desc_en": "Decompilation, hidden API sniffing, agent skill security auditing, pentesting",
        "desc_th": "ถอดรหัสโปรแกรม, แกะ API เบื้องหลังเว็บ, ตรวจความปลอดภัย Skill AI, เจาะระบบทดสอบ",
        "repos": [
            "https://github.com/morluto/rea.git",
            "https://github.com/vxcontrol/pentagi.git",
            "https://github.com/h4ckf0r0day/obscura.git",
            "https://github.com/NVIDIA/SkillSpector.git",
            "https://github.com/D4Vinci/Scrapling.git"
        ],
        "pip": []
    },
    "5": {
        "title_en": "⚙️ Web Automation, Scraping & Desktop Agent Interface",
        "title_th": "⚙️ Web Automation, ดูดข้อมูลเว็บ & คุมหน้าจอเดสก์ท็อป",
        "desc_en": "Headless browser automation, autonomous OS agent, cross-drive skill sync",
        "desc_th": "ควบคุมเบราว์เซอร์อัตโนมัติ, บ็อตเปิดหน้าจอทำงานแทน, ซิงค์คำสั่งข้ามไดรฟ์",
        "repos": [
            "https://github.com/vercel-labs/agent-desktop.git",
            "https://github.com/davidoceanstream/scmdsolution.git",
            "https://github.com/browser-use/browser-use.git"
        ],
        "pip": ["playwright"]
    }
}

def clean_cache():
    virtuoso_path = os.path.join(TOOLS_DIR, "virtuoso", "virtuoso.py")
    if os.path.exists(virtuoso_path):
        print("\n🧹 Purging system & workspace caches with Virtuoso...")
        subprocess.run([sys.executable, virtuoso_path, "clean-cache"])

def sync_skills():
    sync_script = os.path.join(TOOLS_DIR, "scmdsolution", "sync-skills.ps1")
    if os.path.exists(sync_script):
        print("\n⚡ Synchronizing slash commands across AI agents via /scmdsolution...")
        subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", sync_script, "-ToolsDir", TOOLS_DIR, "-Agent", "All"])

def clone_repo(url):
    repo_name = url.split("/")[-1].replace(".git", "")
    target_path = os.path.join(TOOLS_DIR, repo_name)
    if os.path.exists(target_path):
        print(f"  [✓] Repository already exists: {target_path}")
        return True
    print(f"  📥 Cloning {repo_name} into {target_path}...")
    res = subprocess.run(["git", "clone", url, target_path])
    return res.returncode == 0

def install_preset(choice):
    preset = PRESETS.get(str(choice))
    if not preset:
        print(f"❌ Invalid preset choice: {choice}")
        return False

    print(f"\n=======================================================")
    print(f" 🚀 INSTALLING: {preset['title_en']}")
    print(f" 🇹🇭 {preset['title_th']}")
    print(f"=======================================================")
    print(f"Overview: {preset['desc_en']}\n")

    # 1. Repos
    print(f"--- [1/3] Cloning Git Repositories into {TOOLS_DIR} ---")
    for r in preset["repos"]:
        clone_repo(r)

    # 2. Pip
    if preset["pip"]:
        print("\n--- [2/3] Checking / Installing Python Packages ---")
        for pkg in preset["pip"]:
            print(f"  📦 Pip package: {pkg}...")
            subprocess.run([sys.executable, "-m", "pip", "install", pkg, "--quiet"])

    # 3. Sync
    print("\n--- [3/3] Syncing Slash Commands to AI IDEs ---")
    sync_skills()

    # 4. Clean
    clean_cache()

    print("\n=======================================================")
    print(" ✨ Toolkit installation complete! Ready for production.")
    print("=======================================================\n")
    return True

def search_and_install():
    if not os.path.exists(CATALOG_PATH):
        print("❌ Cannot find full_catalog_data.json")
        return

    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        tools = json.load(f)

    keyword = input("\n🔍 Search tool name, keyword, or domain (e.g. whisper, video, security): ").strip().lower()
    if not keyword:
        return

    matches = [t for t in tools if keyword in t.get("name", "").lower() or keyword in t.get("repo", "").lower() or keyword in t.get("brief", "").lower()]

    if not matches:
        print(f"❌ No tools matched: '{keyword}'")
        return

    print(f"\nFound {len(matches)} matching tool(s):")
    for i, m in enumerate(matches, 1):
        status = "🟢 Installed" if m.get("installed_pc1") else "🟡 In Vault"
        print(f"  [{i}] {m['name']} ({status})")
        print(f"      Git: {m['url']}")
        print(f"      Brief: {m.get('brief', '')[:85]}...\n")

    pick = input(f"Enter number to install (1-{len(matches)}) or press Enter to cancel: ").strip()
    if pick.isdigit() and 1 <= int(pick) <= len(matches):
        chosen = matches[int(pick) - 1]
        print(f"\n🚀 Installing: {chosen['name']}...")
        clone_repo(chosen["url"])
        sync_skills()
        clean_cache()
        print(f"✨ Successfully installed {chosen['name']}!")

def interactive_menu():
    while True:
        print("\n=================================================================")
        print(" 🏛️ THE VIRTUOSO - UNIVERSAL AI TOOLKIT 1-CLICK INSTALLER")
        print(" (Global Bilingual Edition: English / ภาษาไทย)")
        print("=================================================================")
        print(" Select a target toolkit preset for your current project:")
        print("-----------------------------------------------------------------")
        for k, v in PRESETS.items():
            print(f"  [{k}] {v['title_en']}")
            print(f"      🇹🇭 {v['title_th']}")
        print("-----------------------------------------------------------------")
        print("  [S] 🔍 Search & select from all 142 tools in Vault (ค้นหาในคลัง)")
        print("  [A] ⚡ Sync all slash commands now via /scmdsolution (ซิงค์คำสั่ง)")
        print("  [C] 🧹 Purge temp files & pip caches via Virtuoso (ล้างขยะ)")
        print("  [Q] Quit (ออกจากโปรแกรม)")
        print("=================================================================")

        choice = input("👉 Enter choice (1-5, S, A, C, Q): ").strip().upper()

        if choice in PRESETS:
            install_preset(choice)
        elif choice == "S":
            search_and_install()
        elif choice == "A":
            sync_skills()
        elif choice == "C":
            clean_cache()
        elif choice == "Q":
            print("\nExiting Virtuoso Installer. Happy building!")
            break
        else:
            print("❌ Invalid option. Please try again.")

def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Virtuoso Universal AI Toolkit Installer")
    parser.add_argument("--preset", type=str, help="Preset number (1-5) to install non-interactively")
    parser.add_argument("--install", type=str, help="Direct Git repo URL or tool name to clone and sync")
    parser.add_argument("--sync", action="store_true", help="Sync slash commands via scmdsolution")
    parser.add_argument("--clean", action="store_true", help="Clean caches via Virtuoso")
    parser.add_argument("--list", action="store_true", help="List all available presets")

    args = parser.parse_args()

    if args.list:
        print("\nAvailable Presets:")
        for k, v in PRESETS.items():
            print(f"  [{k}] {v['title_en']}")
        return

    if args.preset:
        install_preset(args.preset)
        return

    if args.install:
        clone_repo(args.install)
        sync_skills()
        clean_cache()
        return

    if args.sync:
        sync_skills()
        return

    if args.clean:
        clean_cache()
        return

    interactive_menu()

if __name__ == "__main__":
    main()
