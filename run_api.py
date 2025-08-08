#!/usr/bin/env python3
"""
E-WebSearch API 服务启动脚本
"""

import argparse
import os
import sys
from pathlib import Path

import uvicorn
from dotenv import load_dotenv


def main():
    """主函数"""
    # 将项目根目录添加到 sys.path
    project_root = Path(__file__).parent
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

    # 加载环境变量
    env_path = project_root / ".env"
    if env_path.exists():
        print(f"📁 加载环境配置: {env_path}")
        load_dotenv(env_path)
    else:
        print("⚠️  未找到 .env 文件，使用默认配置")

    parser = argparse.ArgumentParser(description="E-WebSearch API 服务")
    parser.add_argument("--host", default="0.0.0.0", help="服务器主机地址")
    parser.add_argument("--port", type=int, default=8000, help="服务器端口")
    parser.add_argument("--reload", action="store_true", help="启用热重载")
    parser.add_argument("--log-level", default="info", help="日志级别")
    parser.add_argument("--workers", type=int, default=1, help="工作进程数")

    args = parser.parse_args()

    print("🚀 启动 E-WebSearch API 服务")
    print(f"📍 地址: http://{args.host}:{args.port}")
    print(f"📚 文档: http://{args.host}:{args.port}/docs")
    print(f"📖 ReDoc: http://{args.host}:{args.port}/redoc")
    print("=" * 50)

    # 启动服务
    uvicorn.run(
        "api.main:app",
        host=args.host,
        port=args.port,
        reload=args.reload,
        log_level=args.log_level,
        workers=args.workers if not args.reload else 1,
    )


if __name__ == "__main__":
    main()
