import torch
import torch.nn as nn
import os
from django.conf import settings
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification,AutoTokenizer, AutoModelForSequenceClassification

# Hugging Face Hub에 올린 모델 경로
model_name = "ksj1234/rangers_model"

# 모델과 토크나이저 불러오기
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

model.eval()  # 평가 모드로 설정

# model_path = os.path.join(os.path.dirname(__file__), 'Add_beomi_model.pt')
# model = AutoModelForSequenceClassification.from_pretrained('beomi/kcbert-base')
# model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
# model.eval()
# tokenizer = AutoTokenizer.from_pretrained('beomi/kcbert-base')

# 새로운 문장을 분류하는 함수를 정의합니다.
def classify_sentence(sentence):
    inputs = tokenizer.encode_plus(
        sentence,
        add_special_tokens=True,
        max_length=128,
        padding='max_length',
        truncation=True,
        return_tensors='pt'
    )
    input_ids = inputs['input_ids']
    attention_mask = inputs['attention_mask']
    # 추론을 수행합니다.
    with torch.no_grad():
        outputs = model(input_ids, attention_mask=attention_mask)
        logits = outputs.logits
    # 소프트맥스 활성화 함수를 적용하고 예측된 클래스를 가져옵니다.
    probabilities = nn.functional.softmax(logits, dim=1)
    predicted_class = torch.argmax(probabilities, dim=1)
    return predicted_class.item()