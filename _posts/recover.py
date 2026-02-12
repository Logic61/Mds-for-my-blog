import os

# --- 配置区 ---
# 指向你现在那堆带有 LOADING 字样的 md 文件夹
MD_DIR = r'C:\Users\32372\recover'

# 定义要删除的“垃圾行”关键词
# 只要行内包含这些词，整行都会被删掉
TRASH_KEYWORDS = [
    "## LOADING",
    "加载过慢请开启缓存",
    "browser-warning",
    "loading.gif",
    "LOGIC の 博客",
    "[ __ Home ]",
    "[ __ About ]",
    "[ __ Archives ]",
    "[ __ Categories ]",
    "[ __ Tags ]",
    "____ Home",
    "____ About"
    "![](/images/loading.gif)"
    "Based on the [Hexo Engine](https://hexo.io) & [ParticleX Theme](https://github.com/theme-particlex/hexo-theme-particlex)"
    "(C) 2022 - 2026 Logic の 博客  __ @Logic "
]

def clean_md_files():
    print("开始清理 MD 文件中的冗余信息...")
    
    count = 0
    for root, dirs, files in os.walk(MD_DIR):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                    
                    # 过滤逻辑：只保留不包含垃圾关键词的行
                    new_lines = []
                    for line in lines:
                        if not any(key in line for key in TRASH_KEYWORDS):
                            new_lines.append(line)
                    
                    # 写回文件
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.writelines(new_lines)
                    
                    print(f"已清洗: {file}")
                    count += 1
                except Exception as e:
                    print(f"无法处理文件 {file}: {e}")

    print(f"\n清理完成。共处理 {count} 个文件。")

if __name__ == "__main__":
    clean_md_files()