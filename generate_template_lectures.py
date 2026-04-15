import os

base_dir = "/Users/mobilelive-ml-lpt-0113/Desktop/Video-lectures"
directories = ["O-Level Subjects", "A-Level Subjects"]

lecture_template = """# Complete Lecture: {topic} ({subject})

Welcome to today's essential lecture on **{topic}**. 
This module forms a critical component of the Cambridge {subject} syllabus and is designed to provide you with a comprehensive understanding of the core concepts, theories, and practical applications required for examination success.

## 1. Introduction and Core Concepts
To begin mastering {topic}, we must first establish the fundamental principles. By understanding the foundational building blocks of this subject, students can construct more complex arguments and solve advanced problems effortlessly.
* **Key Definition:** The primary definition relevant to this sector of {subject}.
* **Relevance:** Why this matters in a real-world context.

## 2. Theoretical Frameworks
When we analyze {topic}, we apply specific theoretical frameworks established in the {subject} curriculum. Focus on breaking down the primary mechanisms, structures, or methodologies here.
> *Teacher's Note: Always remember to cross-reference these concepts with your syllabus guidelines.*

## 3. Practical Examples and Application
Let's look at an example. When applying the principles of {topic} in practice, you'll observe patterns that align directly with past examination questions.
1. Identify the core issue in the scenario.
2. Apply the relevant formula, theory, or historical context.
3. Conclude with a clear, concise evaluation.

## Summary & Next Steps
You have now covered the essentials of {topic}. 
* Make sure you revise these core definitions.
* Attempt at least two past-paper questions focusing specifically on this module.

**Class Dismissed!**
"""

voiceover_template = """# Voice-Over Script: {topic} ({subject})

**[Visual: Upbeat, modern educational intro plays. The title card appears: "Cambridge {subject}: {topic}. Welcome to Class!"]**

**Narrator (Upbeat and clear):**
"Welcome back, students! Today we are diving into an incredibly important area of your {subject} syllabus: **{topic}**. Understanding these core principles is absolutely essential for mastering the curriculum."

**[Visual: Transition to a sleek on-screen graphic highlighting the main definitions of {topic}.]**

**Narrator:**
"Before we get into the complex scenarios, let's look at the absolute fundamentals. What exactly are we dealing with? Just like building a house, you need a solid foundation before you build the walls. In {topic}, our foundation involves mastering the initial variables and definitions."

**[Visual: An engaged, animated infographic illustrating a real-world example of the concept.]**

**Narrator:**
"Let's bring this to life with a real-world application. As you can see on screen, when we encounter a typical problem in {topic}, the best approach is to systematically break it down. Identify your variables, apply your syllabus knowledge, and draw a logical conclusion."

**[Visual: Fast-paced montage of past-paper examples resolving cleanly into a 'pass' mark.]**

**Narrator:**
"At the end of the day, your goal is to translate this knowledge into your exams! The best way to solidify what you've learned here is straight practice. Take the theories we covered today and apply them to standard past-paper scenarios."

**[Visual: The presenter returns on screen / Outro animation starts rolling with key takeaways.]**

**Narrator:**
"And there you have it: the key essentials of {topic}. Take an active approach to your revision, and you'll do great! Thanks for watching, and stay curious!"

**[Visual: Fade to black. End screen.]**
"""

success_count = 0

for d in directories:
    dir_path = os.path.join(base_dir, d)
    if not os.path.exists(dir_path):
        continue
        
    for subject_folder in os.listdir(dir_path):
        subject_path = os.path.join(dir_path, subject_folder)
        if not os.path.isdir(subject_path):
            continue
            
        for topic_folder in os.listdir(subject_path):
            topic_path = os.path.join(subject_path, topic_folder)
            if not os.path.isdir(topic_path):
                continue
                
            lecture_file = os.path.join(topic_path, "01_Lecture.md")
            voiceover_file = os.path.join(topic_path, "02_VoiceOver.md")
            
            # Write a high-quality template specifically adapted to the folder name
            if not os.path.exists(lecture_file):
                with open(lecture_file, 'w', encoding='utf-8') as f:
                    f.write(lecture_template.format(topic=topic_folder, subject=subject_folder))
                    
            if not os.path.exists(voiceover_file):
                with open(voiceover_file, 'w', encoding='utf-8') as f:
                    f.write(voiceover_template.format(topic=topic_folder, subject=subject_folder))
                    
            success_count += 1

print(f"Instantly generated offline templates for {success_count} topics!")
