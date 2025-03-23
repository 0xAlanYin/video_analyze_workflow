from flask import Blueprint, render_template, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
import requests
import json
import os
from .forms import VideoAnalyzeForm

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    form = VideoAnalyzeForm()
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            return redirect(url_for('auth.login'))
        
        if current_user.points < 1:
            flash('积分不足，无法解析视频')
            return redirect(url_for('main.index'))
        
        try:
            # 从环境变量获取API密钥和工作流ID
            coze_api_key = os.getenv('COZE_API_KEY')
            coze_workflow_id = os.getenv('COZE_WORKFLOW_ID')
            
            if not coze_api_key or not coze_workflow_id:
                flash('未配置Coze API密钥或工作流ID，请检查.env文件')
                return redirect(url_for('main.index'))
            
            # 调用 Coze API
            headers = {
                'Authorization': f'Bearer {coze_api_key}',
                'Content-Type': 'application/json'
            }
            data = {
                'parameters': {
                    'input': form.url.data
                },
                'workflow_id': coze_workflow_id
            }
            response = requests.post(
                'https://api.coze.cn/v1/workflow/run',
                headers=headers,
                json=data
            )
            
            result = response.json()
            if result['code'] == 0:
                # 解析成功，扣除积分
                current_user.deduct_points(1)
                output = json.loads(result['data'])['output']
                flash(f'解析结果: {output}')
            else:
                flash('解析失败，请稍后重试')
                
        except Exception as e:
            flash(f'发生错误: {str(e)}')
            
    return render_template('index.html', form=form) 