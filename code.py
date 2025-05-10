from langgraph import LangGraph
import openai
openai.api_key = ''
class ComplaintClassifier:
   def __init__(self):
       self.langgraph = LangGraph()
       self.categories = {
           'service_delays': 'تأخير في الخدمة',
           'staff_behavior': 'سلوك موظف',
           'technical_issues': 'مشاكل تقنية',
           'positive_feedback': 'ملاحظات إيجابية',
           'others': 'أخرى'
       }
   def classify_complaint(self, complaint_text):
       complaint_text = self.preprocess_text(complaint_text)
       classification = self.get_openai_classification(complaint_text)
       return self.categories.get(classification, 'غير معروف')
   def preprocess_text(self, text):
       return text.lower()
   def get_openai_classification(self, text):
       response = openai.Completion.create(
           model="gpt-3.5-turbo",
           prompt=f"Classify the following patient complaint into one of these categories: 'Service Delays', 'Staff Behavior', 'Technical Issues', 'Positive Feedback', or 'Others'. Complaint: {text}",
           max_tokens=50
       )
       return response.choices[0].text.strip().lower()
complaint_classifier = ComplaintClassifier()
# Sample complaints
complaints = [
   "الخدمة كانت بطيئة جدًا وكنت في انتظار طويل.",
   "الموظف كان غير مهذب في تعامله.",
   "واجهت مشكلة في التطبيق أثناء الحجز.",
   "شكراً لكم على الخدمة الممتازة."
]
# Classify each complaint
for complaint in complaints:
   category = complaint_classifier.classify_complaint(complaint)
   print(f"Complaint: {complaint}\nClassified as: {category}\n")
