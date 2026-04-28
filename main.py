# Format IE Report with proper HTML for Google Docs
import datetime

report_content = input_data.get('report_content', '')
report_topic = input_data.get('report_topic', '')
student_email = input_data.get('student_email', '')
student_name = input_data.get('student_name', '')

# Create IE Format Report with HTML styling
# Google Docs supports HTML: heading tags (h1-h6), bold, italic, links, etc.
formatted_report = f"""<p style="font-family: Times New Roman; font-size: 12pt; text-align: center; line-height: 1.15;">
<b style="font-size: 14pt;">{report_topic}</b>
</p>

<p style="font-family: Times New Roman; font-size: 12pt; text-align: justify; line-height: 1.15;">
<b style="font-size: 14pt;">Generated Report</b><br/>
Student: {student_name}<br/>
Email: {student_email}<br/>
Date: {datetime.datetime.now().strftime('%d-%m-%Y')}
</p>

<p style="font-family: Times New Roman; font-size: 12pt; text-align: justify; line-height: 1.15;">
{report_content}
</p>

<p style="font-family: Times New Roman; font-size: 10pt; text-align: center; line-height: 1.15;">
--- End of Report ---
</p>"""

return {
    'formatted_report': formatted_report,
    'topic': report_topic,
    'email': student_email,
    'student_name': student_name,
    'filename': f'IE_Report_{report_topic.replace(" ", "_")}.docx'
}