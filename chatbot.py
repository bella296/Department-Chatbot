from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import spacy
spacy.load('en_core_web_sm')
# from spacy.lang.en import English
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot('<b>SGSITS IT CHAT BOT</b>')

# nlp = spacy.load("en_core_web_sm")

chatbot = ChatBot(
    'ChatBot for College Enquiry',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': "Hi there, Welcome to SGSITS! 👋 If you need any assistance, I'm always here.Go ahead and write the number of any query. 😃✨<b><br><br>  Which of the following user groups do you belong to? <br><br>1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br><br>",
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///db_new.sqlite3'   
) 
trainer = ListTrainer(chatbot)

# python app.py
# Training with Personal Ques & Ans 
# conversation = [
# "Hi",
# "Helloo!",
# "Hey",

# "How are you?",
# "I'm good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

# "Great",
# "Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

# "good",
# "Go ahead and write the number of any query. 😃✨ <br> 2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

# "fine",
# "Go ahead and write the number of any query. 😃✨ <br> 2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

# "Thank You",
# "Your Welcome 😄",

# "Thanks",
# "Your Welcome 😄",

# "Bye",
# "Thank You for visiting!..",

# "What do you do?",
# "I am made to give Information about SGSITS college.",

# "What else can you do?",
# "I can help you know more about SGSITS",
    
#     "1",
#     "<b>STUDENT <br>The following are frequently searched terms related to student . Please select one from the options below : <br> <br> 1.1 Curriculars <br>1.2  Extra-Curriculars<br>1.3  Administrative<br>1.4 Examination <br>1.5 Placements </b>",
    
#     "1.1",
#     "<b>  CURRICULAR <br>  These are the top results: <br> <br> 1.1.1  Academic Calendar <br> 1.1.2 Syllabus </b>",
#    "1.1.1",
#     "<b > 1.1.1 Academic Calender<br>The link to Academic Calender👉<a href=" 'http://www.frcrce.ac.in/index.php/academics/academic-calendar' ">Click Here</a> </b>",
#     "1.1.2",
#     "<b> 1.1.2 Syllabus<br>The link to Syllabus 👉 <a href=" 'https://www.sgsits.ac.in/index.php/it-syllabus' ">Click Here</a> </b>",

#     "1.2",
#     "<b>EXTRA-CURRICULAR<br>These are the top results: <br> <br> 1.2.1 Events<br> 1.2.2 Student Chapters <br> 1.2.3 Student's Council</b>",
#     "1.2.1",
#     "<b > 1.2.1 Events<br>The link to Events👉 <a href=" 'http://www.frcrce.ac.in/index.php/students/events-new' ">Click Here</a></b>",
#     "1.2.2",
#     "<b > 1.2.2 Student Chapters<br>The link to Student Chapters👉<a href=" 'http://www.frcrce.ac.in/index.php/students/forums' ">Click Here</a> </b>",
#     "1.2.3",
#     "<b > 1.2.3 Student's Council <br>The link to Student's Council👉 <a href=" 'http://www.frcrce.ac.in/index.php/students/students-council' ">Click Here</a> </b>",

#     "1.3",
#     "<b>1.3 ADMINISTRATIVE<br>These are the top results: <br> <br> 1.3.1 Students Portal<br> 1.3.2 Notices </b>",
#     "1.3.1",
#     "<b> 1.3.1 Students Portal<br>The link to Students Portal👉 <a href=" 'http://granth.fragnel.edu.in:5186/pinfo/index.php' ">Click Here</a> </b>",
#     "1.3.2",
#     "<b> 1.3.2 Notices<br>The link to Notices👉 <a href=" 'http://www.frcrce.ac.in/index.php/students/crce-notices/109-office-administration' ">Click Here</a> </b>",

#     "1.4",
#     "<b > EXAMINATION <br>These are the top results:<br> 1.4.1 Notices<br> 1.4.2 Examination Process <br> 1.4.3 Question Paper Archive </b>",
#     "1.4.1",
#     "<b > 1.4.1 Notices<br>The link to Notices👉 <a href=" 'http://www.frcrce.ac.in/index.php/students/crce-notices/110-examsection' ">Click Here</a> </b>",
#     "1.4.2",
#     "<b > 1.4.2 Examination Process<br>The link to Examination Process👉<a href=" 'http://www.frcrce.ac.in/index.php/academics/examination/exam-process' ">Click Here</a> </b>",
#     "1.4.3",
#     "<b > 1.4.3 Question Paper Archive<br>The link to Archives👉 <a href=" 'http://www.frcrce.ac.in/questionpaper/ArchUE.php' ">Click Here</a> </b>",

#     "1.5",
#     "<b > PLACEMENTS These are the top results:<br> 1.5.1 Placements<br> 1.5.2 Our Recruiters <br> 1.5.3 Placement Statistics </b>",
#     "1.5.1",
#     "<b> 1.5.1 Placements<br>The link to Placements👉 <a href=" 'http://www.frcrce.ac.in/index.php/students/placements/campus-placement-overview' ">Click Here</a> </b>",
#     "1.5.2",
#     "<b> 1.5.2 Our Recruiters<br>The link to Recruiters👉<a href=" 'http://www.frcrce.ac.in/index.php/students/placements/our-recruiters' ">Click Here</a> </b>",
#     "1.5.3",
#     "<b > 1.5.3 Placement Statistics<br>The link to Placement Statistics👉 <a href=" 'http://www.frcrce.ac.in/index.php/students/placements/placement-statistics' ">Click Here</a> </b>",

#     "2",
#     "<b >FACULTY<br>The following are frequently searched terms related to faculty. Please select one from the options below :</br></br>2.1 Portals & Administration<br>2.2  Change Personal Details<br>2.3  Examination </b>",
    
#     "2.1",
#     "<b > PORTALS & ADMINISTRATION These are the top results:<br> 2.1.1 Biometric Attendance System <br>2.1.2 Moodle </b>",
#     "2.1.1",
#     "<b> 2.1.1 Biometric Attendance<br>The link to Biometric Attendance👉<a href=" 'http://samay.fragnel.edu.in:1234/timeo/' ">Click Here</a> </b>",
#     "2.1.2",
#     "<b> 2.1.2 Moodle<br>The link to Moodle👉<a href=" 'http://gyan.fragnel.edu.in:2222/moodle' ">Click Here</a> </b>",

#     "2.2",
#     "<b > CHANGE PERSONAL DETAILS These are the top results:<br> <br> 2.2.1 Site Login <br> </b>",
#     "2.2.1",
#     "<b> 2.2.1 Site Login<br>The link to Site Login👉<a href=" 'http://www.frcrce.ac.in/index.php/component/users/?view=login&Itemid=437' ">Click Here</a> </b>",
   
#     "2.3",
#     "<b > EXAMINATION <br>These are the top results:<br> <br> 2.3.1 Notices<br> 2.3.2 Question Paper Archive </b>",
#     "2.3.1",
#     "<b> 2.3.1 Notices <br>The link to Notices 👉 <a href=" 'http://www.frcrce.ac.in/index.php/students/crce-notices/110-examsection' ">Click Here</a> </b>",
#     "2.3.2",
#     "<b> 2.3.2 Question Paper Archive <br>The link to Archive👉<a href=" 'http://www.frcrce.ac.in/questionpaper/ArchUE.php' ">Click Here</a> </b>",
  
#     "3",
#     "<b> PARENTS <br>The following are frequently searched terms related to Parents. Please select one from the options below : <br> <br> 3.1 About Us <br>3.2 Notices <br>3.3 Fee Payment <br>3.4 Placements </b> " ,

#     "3.1",
#     "<b > ABOUT US<br>These are the top results:<br> <br> 3.1.1 About CRCE<br> 3.1.2 Director's Address <br> 3.1.3 Principal's Address </b>",
#     "3.1.1",
#     "<b > 3.1.1 About CRCE<br>The link to About CRCE👉 <a href=" 'http://www.frcrce.ac.in/index.php/about-us/about-crce' ">Click Here</a> </b>",
#     "3.1.2",
#     "<b > 3.1.2 Director's Address <br>The link to Director's Address👉<a href=" 'http://www.frcrce.ac.in/index.php/about-us/director' ">Click Here</a> </b>",
#     "3.1.3",
#     "<b > 3.1.3 Principal's Address <br>The link to Principal's Address👉 <a href=" 'http://www.frcrce.ac.in/index.php/about-us/principal-frcrce' ">Click Here</a> </b>",

#     "3.2",
#     "<b > NOTICES<br>These are the top results:<br> <br> 3.2.1 All Notices  </b>",
#     "3.2.1",
#     "<b > 3.2.1 All Notices <br>The link to All Notices👉 <a href=" 'http://www.frcrce.ac.in/index.php/students/crce-notices' ">Click Here</a> </b>",

#     "3.3",
#     "<b > ABOUT US<br>These are the top results:<br> <br>3.3.1 Payment Details <br> 3.3.2 Online Payment Portal </b>",
#     "3.3.1",
#     "<b > 3.3.1 Payment Details<br>The link to Payment Details 👉 <a href=" 'http://frcrce.ac.in/attachments/article/248/NEFTForm.pdf' ">Click Here</a> </b>",
#     "3.3.2",
#     "<b > 3.3.2 Payment Portal <br>The link to Payment Portal👉<a href=" 'https://pay.fragnel.edu.in/CRCE/initPay.php' ">Click Here</a> </b>",

#     "3.4",
#     "<b > PLACEMENTS These are the top results:<br> <br>3.4.1 Placements<br> 3.4.2 Our Recruiters <br> 3.4.3 Placement Statistics </b>",
#     "3.4.1",
#     "<b> 3.4.1 Placements<br>The link to Placements👉 <a href=" 'http://www.frcrce.ac.in/index.php/students/placements/campus-placement-overview' ">Click Here</a> </b>",
#     "3.4.2",
#     "<b> 3.4.2 Our Recruiters<br>The link to Recruiters👉<a href=" 'http://www.frcrce.ac.in/index.php/students/placements/our-recruiters' ">Click Here</a> </b>",
#     "3.4.3",
#     "<b > 3.4.3 Placement Statistics<br>The link to Placement Statistics👉 <a href=" 'http://www.frcrce.ac.in/index.php/students/placements/placement-statistics' ">Click Here</a> </b>",

#     "4",
#     "<b VISITORS <br>The following are frequently searched terms related to visitors. Please select one from the options below : <br> <br> 4.1 About Us<br>4.2 Programs We Offer <br>4.3 Student Bodies <br>4.4 Extra-Curricular </b>",
    
#     "4.1",
#     "<b > ABOUT US<br>These are the top results:<br> <br>4.1.1 About CRCE<br> 4.1.2 Director's Address <br> 4.1.3 Principal's Address </b>",
#     "4.1.1",
#     "<b > 4.1.1 About CRCE<br>The link to About CRCE👉 <a href=" 'http://www.frcrce.ac.in/index.php/about-us/about-crce' ">Click Here</a> </b>",
#     "4.1.2",
#     "<b > 4.1.2 Director's Address <br>The link to Director's Address👉<a href=" 'http://www.frcrce.ac.in/index.php/about-us/director' ">Click Here</a> </b>",
#     "4.1.3",
#     "<b > 4.1.3 Principal's Address <br>The link to Principal's Address👉 <a href=" 'http://www.frcrce.ac.in/index.php/about-us/principal-frcrce' ">Click Here</a> </b>",

#     "4.2",
#     "<b > PROGRAMS WE OFFER <br>These are the top results:<br> <br>4.2.1 Under-Graduate <br> 4.2.2 Post-Graduate<br> 4.2.3 Ph.D </b>",
#     "4.2.1",
#     "<b > 4.2.1 Under-Graduate<br>The link to Under-Graduate👉 <a href=" 'http://www.frcrce.ac.in/index.php/admission/under-graduate' ">Click Here</a> </b>",
#     "4.2.2",
#     "<b > 4.2.2 Post-Graduate <br>The link to Post-Graduate👉<a href=" 'http://www.frcrce.ac.in/index.php/admission/post-graduate' ">Click Here</a> </b>",
#     "4.2.3",
#     "<b > 4.2.3 Ph.D <br>The link to Ph.D👉 <a href=" 'http://www.frcrce.ac.in/index.php/admission/phd' ">Click Here</a> </b>",

#     "4.3",
#     "<b > STUDENT BODIES <br>These are the top results:<br> <br>4.3.1 Students Council  <br> 4.3.2 Students Chapter <br> 4.3.3 Students Project Groups </b>",
#     "4.3.1",
#     "<b > 4.3.1 Students Council  <br>The link to Students Council  👉 <a href=" 'http://www.frcrce.ac.in/index.php/students/students-council' ">Click Here</a> </b>",
#     "4.3.2",
#     "<b > 4.3.2 Students Chapter <br>The link to Students Chapter 👉<a href=" 'http://www.frcrce.ac.in/index.php/students/forums' ">Click Here</a> </b>",
#     "4.3.3",
#     "<b > 4.3.3 Students Project Groups <br>The link to Students Project Groups👉 <a href=" 'http://www.frcrce.ac.in/' ">Click Here</a> </b>",

#     "4.4",
#     "<b > EXTRA-CURRICULAR <br>These are the top results:<br> <br>4.4.1 Events  <br> 4.4.2 Institute Innovation Cell </b>",
#     "4.4.1",
#     "<b > 4.4.1 Events    <br>The link to Events   👉 <a href=" 'http://www.frcrce.ac.in/index.php/students/events-new' ">Click Here</a> </b>",
#     "4.4.2",
#     "<b > 4.4.2 Institute Innovation Cell <br>The link to Institute Innovation Cell 👉<a href=" 'https://crceiic.github.io/' ">Click Here</a> </b>",

# ]


conversation = [
"Hi",
"Helloo!",
"Hey",

"How are you?",
"I'm good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"Great",
"Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"good",
"Go ahead and write the number of any query. 😃✨ <br> 2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"fine",
"Go ahead and write the number of any query. 😃✨ <br> 2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"Thank You",
"Your Welcome 😄",

"Thanks",
"Your Welcome 😄",

"Bye",
"Thank You for visiting!..",

"What do you do?",
"I am made to give Information about SGSITS college.",

"What else can you do?",
"I can help you know more about SGSITS",
    
    "1",
    "<b>STUDENT <br>The following are frequently searched terms related to student . Please select one from the options below : <br> <br> 1.1 Curriculars <br>1.2  Extra-Curriculars<br>1.3  Administrative<br>1.4 Examination <br>1.5 Placements </b>",
    
    "1.1",
    "<b>  CURRICULAR <br>  These are the top results: <br> <br> 1.1.1  Academic Calendar <br> 1.1.2 Syllabus </b>",
   "1.1.1",
    "<b > 1.1.1 Academic Calender<br>The link to Academic Calender👉<a href=" 'https://www.sgsits.ac.in/index.php/academics/academic-calendar' ">Click Here</a> </b>",
    "1.1.2",
    "<b> 1.1.2 Syllabus<br>The link to Syllabus 👉 <a href=" 'https://www.sgsits.ac.in/index.php/it-syllabus' ">Click Here</a> </b>",

    "1.2",
    "<b>EXTRA-CURRICULAR<br>These are the top results: <br> <br> 1.2.1 Student's activities<br> 1.2.2 Clubs <br> 1.2.3 Student's Scholarship</b>",
    "1.2.1",
    "<b > 1.2.1 Student's activities<br>The link to Student's activities👉 <a href=" 'https://www.sgsits.ac.in/index.php/students/student-activities' ">Click Here</a></b>",
    "1.2.2",
    "<b > 1.2.2 Clubs<br>The link to Clubs👉<a href=" 'https://www.sgsits.ac.in/index.php/students/clubs' ">Click Here</a> </b>",
    "1.2.3",
    "<b > 1.2.3 Student's Scholarship <br>The link to Student's Scholarship👉 <a href=" 'https://www.sgsits.ac.in/index.php/students/scholarship-merit-and-others' ">Click Here</a> </b>",

    "1.3",
    "<b>1.3 ADMINISTRATIVE<br>These are the top results: <br> <br> 1.3.1 Students Portal<br> 1.3.2 Notices </b>",
    "1.3.1",
    "<b> 1.3.1 Students Portal<br>The link to Students Portal👉 <a href=" 'https://www.google.com/search?q=sgsits+student+login&rlz=1C1CHBF_enIN1026IN1026&oq=&aqs=chrome.0.35i39i362l8.140389518j0j15&sourceid=chrome&ie=UTF-8' ">Click Here</a> </b>",
    "1.3.2",
    "<b> 1.3.2 Notices<br>The link to Notices👉 <a href=" 'https://www.sgsits.ac.in/' ">Click Here</a> </b>",

    "1.4",
    "<b > EXAMINATION <br>These are the top results:<br> 1.4.1 Online Courses<br> 1.4.2 Exam and Results </b>",
    "1.4.1",
    "<b > 1.4.1 Online Courses<br>The link to Online Courses👉 <a href=" 'https://www.sgsits.ac.in/index.php/academics/courses/online-courses' ">Click Here</a> </b>",
    "1.4.2",
    "<b > 1.4.2 Exam and Results<br>The link to Exam and Results👉<a href=" 'https://www.sgsits.ac.in/index.php/academics/exam-ar' ">Click Here</a> </b>",

    "1.5",
    "<b > PLACEMENTS These are the top results:<br> 1.5.1 Placements<br> 1.5.2 Our Recruiters <br> 1.5.3 Placement Records </b>",
    "1.5.1",
    "<b> 1.5.1 Placements<br>The link to Placements👉 <a href=" 'https://www.sgsits.ac.in/index.php/placement/training-and-placement-cell' ">Click Here</a> </b>",
    "1.5.2",
    "<b> 1.5.2 Our Recruiters<br>The link to Recruiters👉<a href=" 'https://www.sgsits.ac.in/index.php/placement/training-and-placement-cell-2' ">Click Here</a> </b>",
    "1.5.3",
    "<b > 1.5.3 Placement Records<br>The link to Placement Records👉 <a href=" 'https://www.sgsits.ac.in/index.php/placement/campus-record' ">Click Here</a> </b>",

    "2",
    "<b >FACULTY<br>The following are frequently searched terms related to faculty. Please select one from the options below :</br></br>2.1 Portals & Administration<br>2.2  Change Personal Details<br>2.3  Examination </b>",
    
    "2.1",
    "<b > About Department<br> These are the top results:<br> 2.1.1 About IT Dept <br>2.1.2 Courses <br> 2.1.3 Time Table </b>",
    "2.1.1",
    "<b> 2.1.1 About IT Dept<br>The link to About IT Dept 👉<a href=" 'https://www.sgsits.ac.in/index.php/it-about-department' ">Click Here</a> </b>",
    "2.1.2",
    "<b> 2.1.2 Courses<br>The link to Courses 👉<a href=" 'https://www.sgsits.ac.in/index.php/it-courses' ">Click Here</a> </b>",
    "2.1.3",
    "<b> 2.1.3 Time Table<br>The link to Time Table 👉<a href=" 'https://www.sgsits.ac.in/index.php/it-time-table' ">Click Here</a> </b>",

    "2.2",
    "<b > Faculty & Staff These are the top results:<br> <br> 2.2.1 Faculties <br> 2.2.2 Staff <br> </b>",
    "2.2.1",
    "<b> 2.2.1 Faculties <br>The link to Faculties 👉<a href=" 'https://www.sgsits.ac.in/index.php/it-faculty-members' ">Click Here</a> </b>",
     "2.2.2",
    "<b> 2.2.2 Staff <br>The link to Staff 👉<a href=" 'https://www.sgsits.ac.in/index.php/it-staff' ">Click Here</a> </b>",
   
    "3",
    "<b> PARENTS <br>The following are frequently searched terms related to Parents. Please select one from the options below : <br> <br> 3.1 About Us <br>3.2 Notices <br>3.3 Fee Payment <br>3.4 Placements </b> " ,

    "3.1",
    "<b > ABOUT US<br>These are the top results:<br> <br> 3.1.1 About SGSITS<br> 3.1.2 Director's Address <br> 3.1.3 Administration </b>",
    "3.1.1",
    "<b > 3.1.1 About SGSITS<br>The link to About SGSITS👉 <a href=" 'https://www.sgsits.ac.in/index.php/about-institute' ">Click Here</a> </b>",
    "3.1.2",
    "<b > 3.1.2 Director's Address <br>The link to Director's Address👉<a href=" 'https://www.sgsits.ac.in/index.php/about-institute/director-s-message' ">Click Here</a> </b>",
    "3.1.3",
    "<b > 3.1.3 Administration <br>The link to Administration👉 <a href=" 'https://www.sgsits.ac.in/index.php/about-institute/administration' ">Click Here</a> </b>",

    "3.2",
    "<b > NOTICES<br>These are the top results:<br> <br> 3.2.1 All Notices  </b>",
    "3.2.1",
    "<b > 3.2.1 All Notices <br>The link to All Notices👉 <a href=" 'https://www.sgsits.ac.in/' ">Click Here</a> </b>",

    "3.3",
    "<b > ABOUT Dept and Facilities<br>These are the top results:<br> <br>3.3.1 About IT Dept <br> 3.3.2 Facilities</b>",
    "3.3.1",
    "<b > 3.3.1 About IT Dept<br>The link to About IT Dept 👉 <a href=" 'https://www.sgsits.ac.in/index.php/departments/information-technology' ">Click Here</a> </b>",
    "3.3.2",
    "<b > 3.3.2 Facilities <br>The link to Facilities👉<a href=" 'https://www.sgsits.ac.in/index.php/it-facilities' ">Click Here</a> </b>",

    "3.4",
    "<b > PLACEMENTS <br>These are the top results:<br> <br>3.4.1 Placements<br> 3.4.2 Our Recruiters <br> 3.4.3 Placement Records </b>",
    "3.4.1",
    "<b> 3.4.1 Placements<br>The link to Placements👉 <a href=" 'https://www.sgsits.ac.in/index.php/placement/training-and-placement-cell' ">Click Here</a> </b>",
    "3.4.2",
    "<b> 3.4.2 Our Recruiters<br>The link to Our Recruiters👉<a href=" 'https://www.sgsits.ac.in/index.php/placement/training-and-placement-cell-2' ">Click Here</a> </b>",
    "3.4.3",
    "<b > 3.4.3 Placement Records<br>The link to Placement Records👉 <a href=" 'https://www.sgsits.ac.in/index.php/placement/campus-record' ">Click Here</a> </b>",

    "3.5",
    "<b > Hostels & Accomadation <br>These are the top results:<br> <br>3.5.1 Boys Hostel  <br> 3.5.2 Girls Hostel <br> 3.5.3 Transit Hostel <br> 3.5.4 Guest House <br> 3.5.5 Staff Quarters </b>",
    "3.5.1",
    "<b > 3.5.1 Boys Hostel <br>The link to Boys Hostel👉 <a href=" 'https://www.sgsits.ac.in/index.php/hostel-accommodation/boys-hostel' ">Click Here</a> </b>",
    "3.5.2",
    "<b > 3.5.2 Girls Hostel <br>The link to Girsl Hostel👉<a href=" 'https://www.sgsits.ac.in/index.php/hostel-accommodation/girls-hostel' ">Click Here</a> </b>",
    "3.5.3",
    "<b > 3.5.3 Transit Hostel <br>The link to Transit Hostel👉 <a href=" 'https://www.sgsits.ac.in/index.php/hostel-accommodation/transit-hostel' ">Click Here</a> </b>",
    "3.5.4",
    "<b > 3.5.4 Guest House <br>The link to Students Guest House👉 <a href=" 'https://www.sgsits.ac.in/index.php/hostel-accommodation/guest-house' ">Click Here</a> </b>",
    "3.5.5",
    "<b > 3.5.5 Staff Quarters <br>The link to Students Staff Quarters👉 <a href=" 'https://www.sgsits.ac.in/index.php/hostel-accommodation/staff-quarters' ">Click Here</a> </b>",


    "4",
    "<b VISITORS <br>The following are frequently searched terms related to visitors. Please select one from the options below : <br> <br> 4.1 About Us<br>4.2 Programs We Offer <br>4.3 Student Bodies <br>4.4 Extra-Curricular </b>",
    
    "4.1",
    "<b > ABOUT US<br>These are the top results:<br> <br>4.1.1 About SGSITS<br> 4.1.2 Director's Address <br> 4.1.3 Administration </b>",
    "4.1.1",
    "<b > 4.1.1 About SGSITS<br>The link to About SGSITS👉 <a href=" 'https://www.sgsits.ac.in/index.php/about-institute' ">Click Here</a> </b>",
    "4.1.2",
    "<b > 4.1.2 Director's Address <br>The link to Director's Address👉<a href=" 'https://www.sgsits.ac.in/index.php/about-institute/director-s-message' ">Click Here</a> </b>",
    "4.1.3",
    "<b > 4.1.3 Administration <br>The link to Administration👉 <a href=" 'https://www.sgsits.ac.in/index.php/about-institute/administration' ">Click Here</a> </b>",

    "4.2",
    "<b > PROGRAMS WE OFFER <br>These are the top results:<br> <br>4.2.1 Under-Graduate <br> 4.2.2 Post-Graduate<br> 4.2.3 Ph.D </b>",
    "4.2.1",
    "<b > 4.2.1 Under-Graduate<br>The link to Under-Graduate👉 <a href=" 'https://www.sgsits.ac.in/index.php/admission/ug-admission' ">Click Here</a> </b>",
    "4.2.2",
    "<b > 4.2.2 Post-Graduate <br>The link to Post-Graduate👉<a href=" 'https://www.sgsits.ac.in/index.php/admission/pg-admission' ">Click Here</a> </b>",
    "4.2.3",
    "<b > 4.2.3 Ph.D <br>The link to Ph.D👉 <a href=" 'https://www.sgsits.ac.in/index.php/admission/ph-d-admission' ">Click Here</a> </b>",

    "4.3",
    "<b > Hostels & Accomadation <br>These are the top results:<br> <br>4.3.1 Boys Hostel  <br> 4.3.2 Girls Hostel <br> 4.3.3 Transit Hostel <br> 4.3.4 Guest House <br> 4.3.5 Staff Quarters </b>",
    "4.3.1",
    "<b > 4.3.1 Boys Hostel <br>The link to Boys Hostel👉 <a href=" 'https://www.sgsits.ac.in/index.php/hostel-accommodation/boys-hostel' ">Click Here</a> </b>",
    "4.3.2",
    "<b > 4.3.2 Girls Hostel <br>The link to Girsl Hostel👉<a href=" 'https://www.sgsits.ac.in/index.php/hostel-accommodation/girls-hostel' ">Click Here</a> </b>",
    "4.3.3",
    "<b > 4.3.3 Transit Hostel <br>The link to Transit Hostel👉 <a href=" 'https://www.sgsits.ac.in/index.php/hostel-accommodation/transit-hostel' ">Click Here</a> </b>",
    "4.3.4",
    "<b > 4.3.4 Guest House <br>The link to Students Guest House👉 <a href=" 'https://www.sgsits.ac.in/index.php/hostel-accommodation/guest-house' ">Click Here</a> </b>",
    "4.3.5",
    "<b > 4.3.5 Staff Quarters <br>The link to Students Staff Quarters👉 <a href=" 'https://www.sgsits.ac.in/index.php/hostel-accommodation/staff-quarters' ">Click Here</a> </b>",

    "4.4",
    "<b > EXTRA-CURRICULAR <br>These are the top results:<br> <br>4.4.1 Student Activities <br> 4.4.2 Clubs </b>",
    "4.4.1",
    "<b > 4.4.1 Student Activities <br>The link to Student Activities👉 <a href=" 'https://www.sgsits.ac.in/index.php/students/student-activities' ">Click Here</a> </b>",
    "4.4.2",
    "<b > 4.4.2 Clubs <br>The link to Clubs 👉<a href=" 'https://www.sgsits.ac.in/index.php/students/clubs' ">Click Here</a> </b>",

]

trainer.train(conversation)
