# 视频解析平台

一个基于 Flask 的视频解析平台，支持用户注册、登录、积分系统和视频解析功能。

## 功能特点

- 用户认证系统（注册、登录、退出）
- 积分系统
  - 新用户注册赠送 10 积分
  - 每日首次登录奖励 10 积分
  - 每次解析扣除 1 积分
- 视频解析功能
- 响应式界面设计

## 安装说明

1. 克隆项目：
```bash
git clone [repository-url]
cd video-analyze-platform
```

2. 创建虚拟环境：
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

4. 配置环境变量：
复制 `.env.example` 到 `.env` 并修改配置

5. 运行应用：
```bash
flask run
```

## 使用说明

1. 访问 http://localhost:5000
2. 注册新账号或登录已有账号
3. 在首页输入视频链接进行解析
4. 查看解析结果

## 技术栈

- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-WTF
- Bootstrap 5
- SQLite 