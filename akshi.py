import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_bulk_emails(df_top15, sender_email, app_password):
    """
    Sends a professional reminder email to each shortlisted candidate.
    df_top15 should have columns: candidate_name, candidate_email
    """

    try:
        # Setup SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)

        for _, row in df_top15.iterrows():
            name = row.get("candidate_name", "Candidate").strip()
            email = row.get("candidate_email", "").strip()

            if not email:
                continue  # Skip if email is missing

            # --- Email Content ---
            subject = "Reminder: XYZ Company Internship Drive — Online Test on 4 Nov 2025"

            body = f"""
Dear {name or "Candidate"},

Congratulations 🎉🎉 once again on being shortlisted for the **XYZ Company Full Stack Engineering Internship Drive (Jan 2026)**.

This email serves as a **gentle reminder** for your **online test scheduled for tomorrow, 4 November 2025, at 12:00 PM IST**.  
Please review the following details carefully to ensure a smooth test experience.

---

🗓 **Test Details**
- **Date:** 4 November 2025  
- **Time:** 12:00 PM IST  
- **Duration:** 30 minutes  
- **Test Window:** 12:00 PM – 12:45 PM IST  
- **Assessment Portal:** https://quiz.xyzcompany.com/

---

🧭 **Before the Test**
1. Visit the Assessment Portal: https://quiz.xyzcompany.com/  
2. Authenticate yourself using the same registered email ID.  
3. Once verified, you will be redirected to the Test Page containing detailed instructions.  
4. The “Start Test” button will become active at **11:55 AM IST** on 4 November 2025.  
5. Please use the **same laptop or system** you used during authentication. If you switch devices, you will need to authenticate again.

---

⚠️ **Note on Conduct**
The test platform is monitored for any form of malpractice.  
Any suspicious behavior or multiple logins may lead to **disqualification**, even after submission.

---

💬 **For Support**
If you encounter login or technical issues, please reach out only through our **Support Form**:  
[Support Form Link](https://support.xyzcompany.com/internship-drive)

---

Wishing you all the very best for your assessment tomorrow.  
We look forward to seeing you perform well.

Warm regards,  
**HR Team**  
**XYZ Company**
"""

            # Prepare MIME message
            msg = MIMEMultipart()
            msg["From"] = sender_email
            msg["To"] = email
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))

            # Send email
            server.sendmail(sender_email, email, msg.as_string())
            print(f"📧 Email sent to {name} ({email})")

        server.quit()
        print("✅ All emails sent successfully!")

    except Exception as e:
        print(f"❌ Error while sending emails: {e}")
