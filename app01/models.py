from django.db import models

class ChatHistory(models.Model):
    send_user_id = models.IntegerField(verbose_name='发送者ID')
    content = models.TextField(verbose_name='聊天内容')
    is_ai_sent = models.BooleanField(default=False, verbose_name="由AI发送")  # 默认为False，表明非AI发送
    send_time = models.DateTimeField(verbose_name='发送时间', auto_now_add=True)

    # def __str__(self):
    #     return f"Message from user {self.send_user_id} at {self.send_time}"

    # class Meta:
    #     verbose_name = '聊天历史'
    #     verbose_name_plural = '聊天历史'

class UploadForm(models.Model):
    upload_id = models.IntegerField(verbose_name='上传者ID')
    img = models.FileField(verbose_name='上传内容')
    img_name = models.CharField(verbose_name='文件名',max_length= 155,default="png")
    status = models.CharField(verbose_name="状态",max_length=100)