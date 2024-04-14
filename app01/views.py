from django.shortcuts import render,HttpResponse
from app01.models import ChatHistory,UploadForm
from modelscope import snapshot_download
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

from modelscope import AutoModelForCausalLM, AutoTokenizer
from modelscope import GenerationConfig

import os

tokenizer = AutoTokenizer.from_pretrained("./model/qwen/Qwen-7B-Chat", trust_remote_code=True)

model = AutoModelForCausalLM.from_pretrained(
    "./model/qwen/Qwen-7B-Chat", 
    device_map="auto",
    trust_remote_code=True, 
    # bf16=True
    ).eval()

# Create your views here.
class ChatSerializer(serializers.Serializer):
    # send_user_id = serializers.IntegerField()
    content = serializers.CharField()
    ai = serializers.BooleanField(source="is_ai_sent")
    time = serializers.DateTimeField(source="send_time", format='%Y-%m-%d %H:%M:%S')

class UploadSerializer(serializers.Serializer):
    upload_id = serializers.IntegerField()
    # img = serializers.FileField()
    img_name = serializers.CharField()
    status = serializers.CharField()
    

def index(request):
    return HttpResponse("欢迎使用")

@api_view(['GET']) 
def download(request):
    model_dir = snapshot_download('qwen/Qwen-7B-Chat',cache_dir='./model')
    return Response({
            "status": {
                "code": 1,
                "msg": "模型下载完了，以后不用再下载了"
            },
            "data": None
        })

@api_view(['POST'])  # 声明这是一个接受 POST 请求的视图函数
def tuili(request):
    if request.method == 'GET':
        return HttpResponse('GET...')
    else:
        userid = request.POST.get('id')
        content = request.POST.get('content')
        if userid is None:
            return Response({
                    "status": {
                        "code": 0,
                        "msg": "请输入正确的id"
                    },
                    "data": None
                })
        else:
            userid = int(userid)
            ChatHistory.objects.create(send_user_id=userid,content=content)
            # inputs = tokenizer(content, return_tensors='pt').to(model.device)
            # print(model.device)
            # pred = model.generate(**inputs)
            # response = tokenizer.decode(pred.cpu()[0], skip_special_tokens=True)
            response, history = model.chat(tokenizer, content, history=None)
            ChatHistory.objects.create(send_user_id=userid, content=response, is_ai_sent = True)
            data_list = ChatHistory.objects.filter(send_user_id=userid)
            serializers = ChatSerializer(instance=data_list, many=True)
            return Response({
                    "status": {
                        "code": 1,
                        "msg": ""
                    },
                    "data": serializers.data
                })


@api_view(['GET'])  # 声明这是一个接受 POST 请求的视图函数
def delete(request):
    userid = request.GET.get("userid")
    print(userid)
    ChatHistory.objects.filter(send_user_id=userid).delete()
    return Response({
                    "status": {
                        "code": 1,
                        "msg": "删除成功"
                    },
                    "data": None
                })

@api_view(['POST'])  # 声明这是一个接受 POST 请求的视图函数
def upload(request):
    if request.method == "GET":
        return Response({
                    "status": {
                        "code": 1,
                        "msg": "请使用POST请求"
                    },
                    "data": None
                })
    else:
        upload_id = int(request.POST.get('id'))
        file_object = request.FILES.get("avatar") # 获取文件对象（包含名字和内容）
        file_name = file_object.name
        print(file_name)
        file_path = os.path.join('media',str(upload_id),file_name)
        print(file_path)
        directory_path = os.path.join('media',str(upload_id))
        print(directory_path)
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
        f = open(file_path, mode='wb')
        for chunk in file_object.chunks():
            f.write(chunk)
        f.close()
        UploadForm.objects.create(upload_id=upload_id, img=file_path, img_name=file_name, status= "学习中")
        data_list = UploadForm.objects.filter(upload_id = upload_id)
        serializers = UploadSerializer(instance=data_list, many=True)
        return Response({
                "status": {
                    "code": 1,
                    "msg": ""
                },
                "data": serializers.data
                })