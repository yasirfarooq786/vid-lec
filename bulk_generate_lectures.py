import os
import time
from google import genai
from google.genai import types

# ==============================================================================
# PREREQUISITES:
# 1. Install the Google GenAI SDK: pip install google-genai
# 2. Set your API key in your terminal before running:
#    export GEMINI_API_KEY="your_api_key_here"
# ==============================================================================

client = genai.Client()

def generate_content(prompt):
    while True:
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.7,
                )
            )
            return response.text
        except Exception as e:
            err_msg = str(e)
            if '429' in err_msg or 'RESOURCE_EXHAUSTED' in err_msg:
                print("  [!] Free tier API rate limit reached. Pausing for 60 seconds to refresh quota...")
                time.sleep(60)
            else:
                print(f"Error generating content: {e}")
                return None

base_dir = "/Users/mobilelive-ml-lpt-0113/Desktop/Video-lectures"
directories = ["O-Level Subjects", "A-Level Subjects"]

print("Starting bulk generation of lectures and voice-overs...")

for d in directories:
    dir_path = os.path.join(base_dir, d)
    if not os.path.exists(dir_path):
        continue
        
    for subject_folder in os.listdir(dir_path):
        subject_path = os.path.join(dir_path, subject_folder)
        if not os.path.isdir(subject_path):
            continue
            
        print(f"\nProcessing Subject: {subject_folder}")
        for topic_folder in os.listdir(subject_path):
            topic_path = os.path.join(subject_path, topic_folder)
            if not os.path.isdir(topic_path):
                continue
                
            lecture_file = os.path.join(topic_path, "01_Lecture.md")
            voiceover_file = os.path.join(topic_path, "02_VoiceOver.md")
            
            # Skip if already generated to save time and API calls
            if os.path.exists(lecture_file) and os.path.exists(voiceover_file):
                continue
                
            print(f"  -> Generating content for: {topic_folder}")
            
            # 1. Generate Lecture
            lecture_prompt = f"Act as an expert teacher. Create a complete, engaging, and detailed lecture/tutorial for the topic '{topic_folder}' in the Cambridge syllabus subject '{subject_folder}'. Explain the topic with examples and use a positive, encouraging teaching style. Format purely in Markdown."
            lecture_content = generate_content(lecture_prompt)
            
            if lecture_content:
                with open(lecture_file, 'w', encoding='utf-8') as f:
                    f.write(lecture_content)
            
            # 2. Generate Voice-Over
            vo_prompt = f"Based on the educational topic '{topic_folder}' in the subject '{subject_folder}', create an upbeat, modern educational voice-over script. Include [Visual: ...] cues for on-screen animations followed by the Narrator's lines. Format purely in Markdown."
            vo_content = generate_content(vo_prompt)
            
            if vo_content:
                with open(voiceover_file, 'w', encoding='utf-8') as f:
                    f.write(vo_content)
                    
            # Pause to respect API rate limits
            time.sleep(4)
            
print("\nBulk generation completed!")
