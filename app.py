import streamlit as st
import json
import os
from cryptography.fernet import Fernet
import hashlib
import requests
import socket

# إنشاء ملفات اللغة
arabic_language = {
    "title": "أكاديمية الأمن السيبراني والبايثون 🛡️🐍",
    "select_section": "اختر القسم التعليمي",
    "python_basics": "أساسيات البايثون",
    "cybersecurity": "الأمن السيبراني",
    "practical_exercises": "تمارين عملية",
    "projects": "مشاريع تطبيقية",
    "syntax": "البناء اللغوي",
    "data_structures": "هياكل البيانات",
    "oop": "البرمجة كائنية التوجه",
    "libraries": "المكتبات",
    "networking": "شبكات الحاسوب",
    "cryptography": "التشفير",
    "web_security": "أمن الويب",
    "ethical_hacking": "الاختراق الأخلاقي",
    "select_exercise": "اختر التمرين",
    "password_checker": "فحص قوة كلمات المرور",
    "port_scanner": "ماسح المنافذ",
    "encryption_tool": "أداة التشفير",
    "vulnerability_analyzer": "محلل الثغرات",
    "enter_password": "أدخل كلمة المرور",
    "password_strength": "قوة كلمة المرور",
    "encrypted_text": "النص المشفر",
    "key": "المفتاح",
    "enter_text": "أدخل النص",
    "encrypt": "تشفير",
    "decrypt": "فك التشفير",
    "select_project": "اختر المشروع",
    "simple_firewall": "جدار حماية بسيط",
    "network_monitor": "مراقب الشبكة",
    "web_scanner": "ماسح المواقع",
    "encryption_app": "تطبيق التشفير",
    "project_guidance": "سنوجهك خطوة بخطوة لبناء هذا المشروع",
    "target_url": "الرابط المستهدف",
    "scan": "فحص",
    "target_ip": "IP العنوان",
    "start_port": "منفذ البداية",
    "end_port": "منفذ النهاية",
    "start_scan": "بدء الفحص",
    "open_ports": "المنافذ المفتوحة"
}

english_language = {
    "title": "Cybersecurity & Python Academy 🛡️🐍",
    "select_section": "Select Learning Section",
    "python_basics": "Python Basics",
    "cybersecurity": "Cybersecurity",
    "practical_exercises": "Practical Exercises",
    "projects": "Practical Projects",
    "syntax": "Syntax",
    "data_structures": "Data Structures",
    "oop": "Object Oriented Programming",
    "libraries": "Libraries",
    "networking": "Networking",
    "cryptography": "Cryptography",
    "web_security": "Web Security",
    "ethical_hacking": "Ethical Hacking",
    "select_exercise": "Select Exercise",
    "password_checker": "Password Strength Checker",
    "port_scanner": "Port Scanner",
    "encryption_tool": "Encryption Tool",
    "vulnerability_analyzer": "Vulnerability Analyzer",
    "enter_password": "Enter Password",
    "password_strength": "Password Strength",
    "encrypted_text": "Encrypted Text",
    "key": "Key",
    "enter_text": "Enter Text",
    "encrypt": "Encrypt",
    "decrypt": "Decrypt",
    "select_project": "Select Project",
    "simple_firewall": "Simple Firewall",
    "network_monitor": "Network Monitor",
    "web_scanner": "Web Scanner",
    "encryption_app": "Encryption Application",
    "project_guidance": "We will guide you step by step to build this project",
    "target_url": "Target URL",
    "scan": "Scan",
    "target_ip": "Target IP",
    "start_port": "Start Port",
    "end_port": "End Port",
    "start_scan": "Start Scan",
    "open_ports": "Open Ports"
}

def load_language(lang):
    """تحميل ملفات اللغة"""
    return arabic_language if lang == "العربية" else english_language

# إعداد واجهة Streamlit
def main():
    st.set_page_config(
        page_title="Cybersecurity & Python Academy",
        page_icon="🛡️",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # شريط جانبي لاختيار اللغة
    with st.sidebar:
        st.title("🌍 الإعدادات / Settings")
        lang = st.radio("اللغة / Language", ["العربية", "English"])
        
        st.markdown("---")
        st.header("🛠️ الأدوات / Tools")
        st.info("تطبيق متكامل لتعلم البايثون والأمن السيبراني" if lang == "العربية" 
               else "Complete application for learning Python and Cybersecurity")
    
    strings = load_language(lang)
    
    # القائمة الرئيسية
    st.sidebar.markdown("---")
    st.sidebar.header("📚 المحتوى التعليمي / Learning Content")
    
    section = st.sidebar.radio(
        strings["select_section"],
        [
            strings["python_basics"],
            strings["cybersecurity"], 
            strings["practical_exercises"],
            strings["projects"]
        ]
    )
    
    # العنوان الرئيسي
    st.title(strings["title"])
    
    # قسم أساسيات البايثون
    if section == strings["python_basics"]:
        st.header("🐍 " + strings["python_basics"])
        
        tabs = st.tabs([
            strings["syntax"],
            strings["data_structures"], 
            strings["oop"],
            strings["libraries"]
        ])
        
        with tabs[0]:
            st.subheader(strings["syntax"])
            st.code('''
# أمثلة على البايثون
print("مرحبا بالعالم!")
name = input("أدخل اسمك: ")
print(f"أهلاً {name}!")
''', language='python')
        
        with tabs[1]:
            st.subheader(strings["data_structures"])
            st.code('''
# القوائم في بايثون
my_list = [1, 2, 3, "hello"]
my_list.append("new item")

# القواميس
person = {"name": "أحمد", "age": 25}
print(person["name"])
''', language='python')
    
    # قسم الأمن السيبراني
    elif section == strings["cybersecurity"]:
        st.header("🛡️ " + strings["cybersecurity"])
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🔐 " + strings["encryption_tool"])
            text = st.text_input(strings["enter_text"], key="encrypt_text")
            
            if st.button(strings["encrypt"]):
                if text:
                    key = Fernet.generate_key()
                    fernet = Fernet(key)
                    encrypted_text = fernet.encrypt(text.encode())
                    
                    st.text_area(strings["encrypted_text"], encrypted_text.decode())
                    st.text_area(strings["key"], key.decode())
                else:
                    st.warning("أدخل نصًا أولاً")
        
        with col2:
            st.subheader("🔍 فحص كلمات المرور")
            password = st.text_input(strings["enter_password"], type="password", key="password_check")
            if password:
                score = 0
                if len(password) >= 8: score += 1
                if any(c.islower() for c in password): score += 1
                if any(c.isupper() for c in password): score += 1
                if any(c.isdigit() for c in password): score += 1
                if any(not c.isalnum() for c in password): score += 1
                
                st.metric(strings["password_strength"], f"{score}/5")
                st.progress(score/5)
    
    # قسم التمارين العملية
    elif section == strings["practical_exercises"]:
        st.header("💻 " + strings["practical_exercises"])
        
        exercise = st.selectbox(strings["select_exercise"], [
            strings["password_checker"],
            strings["port_scanner"]
        ])
        
        if exercise == strings["port_scanner"]:
            st.subheader("🔍 " + strings["port_scanner"])
            st.info("أداة مسح المنافذ التعليمية")
            
            if st.button(strings["start_scan"]):
                st.write("جاري فحص المنافذ...")
                # محاكاة المسح
                open_ports = [80, 443, 22]
                st.success(f"المنافذ المفتوحة: {open_ports}")
    
    # قسم المشاريع
    else:
        st.header("🚀 " + strings["projects"])
        
        project = st.selectbox(strings["select_project"], [
            strings["simple_firewall"],
            strings["encryption_app"]
        ])
        
        st.info(strings["project_guidance"])
        st.code('''
# مثال على مشروع جدار حماية
import socket

class SimpleFirewall:
    def __init__(self):
        self.blocked_ips = ["192.168.1.100"]
    
    def check_packet(self, ip, port):
        if ip in self.blocked_ips:
            return False
        return True
''', language='python')

# تشغيل التطبيق
if __name__ == "__main__":
    main()
