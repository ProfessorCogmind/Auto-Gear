# THIS PROJECT WILL BE A SOMETHING OFF WHICH ALLOWS A BOT TO HANDLE AUTOMATIC EMAILING




# ALL IMPORTS
import os, smtplib, threading, time
from datetime import datetime, timedelta
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



# SERIOUS CODE EDITS BY NSM_Barii Enjoy Nigger




class Email_Controller():
    """This class will be used to control any and all email workflows"""



    # --- RECURRING BACKGROUND WORKER FUNCTION ---
    @classmethod
    def _send_email_worker(cls, scheduled_time, is_recurring, interval_type, interval_value, smtp_server, password, sender, recipients_list, msg_template, temp_file_path):
        """Handles initial delay and loops indefinitely if marked as recurring."""
        
        # 1. Handle Initial Delay (if specified)
        if scheduled_time:
            time_difference = (scheduled_time - datetime.now()).total_seconds()
            if time_difference > 0:
                time.sleep(time_difference)
                
        while True:
            try:

                # Re-establish connection per transmission block to avoid connection timeouts
                bg_server = smtplib.SMTP(smtp_server, 587)
                bg_server.ehlo()
                bg_server.starttls()
                bg_server.ehlo()
                bg_server.login(sender, password)
                
                # Re-generate the message structure to update timestamps if necessary
                bg_server.sendmail(sender, recipients_list, msg_template.as_string())
                print(f"\n\n[Background Job] ##--Email dispatched successfully at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}!--##\n\n")

            except Exception as e:
                print(f"\n[Background Job] Failed to send email: {e}\n")
            finally:
                try:
                    bg_server.quit()
                except:
                    pass

            # 2. Determine Next Cycle
            if not is_recurring:
                # Single-run execution complete; clean up file and exit thread
                if os.path.exists(temp_file_path):
                    try:
                        os.remove(temp_file_path)
                        print("[Background Job] Temporary content file cleaned up.")
                    except:
                        pass
                break
            else:
                # Calculate wait time based on chosen metric
                if interval_type == "minutes": sleep_seconds = interval_value * 60
                elif interval_type == "hours": sleep_seconds = interval_value * 3600
                else:                          sleep_seconds = interval_value * 86400 # "days"
                    
                next_run = datetime.now() + timedelta(seconds=sleep_seconds)
                print(f"[Background Job] Next execution scheduled for: {next_run.strftime('%Y-%m-%d %H:%M:%S')}")
                time.sleep(sleep_seconds)


    
    @classmethod
    def _email_controller(cls, smtp_server, sender, password):
        """This will be called upon from main after all constants have been filled"""



        try:
            test_server = smtplib.SMTP(smtp_server, 587)
            test_server.ehlo()
            test_server.starttls()
            test_server.login(sender, password)
            test_server.quit()
            print("\n\nLogin-Complete\n\nWelcome!\n\n")
        except Exception as e:
            print(f"Initial Login verification failed: {e}")
            exit()

        # MAIN WORKFLOW LOOP
        while True:

            print("\n\nWhat would you like to do:\n")
            print("1. Send / Schedule an email\n2. Send a system log/alert\n3. Exit Program")

            try:
                select = input("\nInput your choice (1, 2, or 3): ")
            except ValueError:
                print("Please enter a valid number.")
                continue

            if select == "3":
                print("Exiting application...")
                break

            if select in ["1", "2"]:
                bot_name = input("Input a Bot name: ").strip()
                msg = MIMEMultipart()
                msg['From'] = f"{bot_name} <{sender}>"

                receiver = input("\nSelect Receiver: ").strip()
                msg['To'] = receiver 

                subject = input("\nWhat is the Subject: ").strip()
                msg['Subject'] = subject 

                content_filename = input("\nInput a name for the temporary text document: ").strip()
                content = input("\nContent of document: ")

                temp_file_path = f"{content_filename}.txt"

                try:

                    with open(temp_file_path, "w") as file:
                        file.write(content) 
                        print(f"\nSuccess! '{temp_file_path}' has been created\n")

                except Exception as e: 
                    print(f"[!] Exception Error: {e}"); exit()


                try:

                    with open(temp_file_path, 'r') as f:
                        email_body = f.read()
                    msg.attach(MIMEText(email_body, 'plain'))

                except Exception as e:
                    print(f"[!] Exception Error: {e}")
                
                attachment_choice = input("\nDo you have an attachment? (y/n): ").strip().lower()
                if attachment_choice in ["yes", "y"]:
                    attachment_filename = input("\nEnter the full filename of the attachment: ").strip()
                    try:
                        with open(attachment_filename, 'rb') as attachment: 
                            p = MIMEBase('application', 'octet-stream')
                            p.set_payload(attachment.read())
                        encoders.encode_base64(p)
                        p.add_header('Content-Disposition', f'attachment; filename={attachment_filename}')
                        msg.attach(p)
                        print("Attachment added successfully!")
                    except FileNotFoundError:
                        print(f"File '{attachment_filename}' not found.")

                bcc_choice = input("\nDo you wish to BCC anyone? (y/n): ").strip().lower()
                recipients_list = [receiver]
                if bcc_choice in ["yes", "y"]:
                    bcc_receiver = input("\nWho would you like to BCC?: ").strip()
                    recipients_list.append(bcc_receiver)

                # RECURRING & SCHEDULING LOGIC
                is_recurring = False
                interval_type = None
                interval_value = 0
                scheduled_time = None

                recurring_choice = input("\nShould this email repeat on a recurring schedule? (y/n): ").strip().lower()
                if recurring_choice in ["yes", "y"]:
                    is_recurring = True
                    print("\nSelect frequency type:\n1. Minutes\n2. Hours\n3. Days")
                    freq_choice = input("Choice (1-3): ").strip()
                    
                    if   freq_choice == "1":    interval_type = "minutes"
                    elif freq_choice == "2":  interval_type = "hours"
                    else:                     interval_type = "days"
                        
                    interval_value = int(input(f"Enter interval frequency value (Every 'X' {interval_type}): "))

                schedule = input("\nDo wish to set a delayed start time for the first delivery? (y/n): ").strip().lower()

                if schedule in ["yes", "y"]:

                    print("\nWhat Day and Time would you like the first email to run?\n")
                    print(" Format: YYYY-MM-DD HH:MM (e.g., 2026-10-25 14:30)")
                    while True:

                        time_input = input("Enter Date & Time: ").strip()

                        try:

                            scheduled_time = datetime.strptime(time_input, "%Y-%m-%d %H:%M")
                            if scheduled_time <= datetime.now():
                                print("Error: That time is in the past!")
                                continue
                            break
                        
                        except ValueError: print("Error: Invalid format. Please use YYYY-MM-DD HH:MM.")

                # DELEGATION
                print("\nSpawning execution thread...")
                threading.Thread(
                    target=cls._send_email_worker,
                    args=(scheduled_time, is_recurring, interval_type, interval_value, smtp_server, password, sender, recipients_list, msg, temp_file_path),
                    daemon=True
                ).start()

                print("Process active in background. Returning to main engine menu.")



    @classmethod
    def main(cls):
        """This is where class will launch from"""


        print("""##---Auto-Gears---##""")

        print("What is your SMTP service?\n\n1. Google\n2. Outlook\n3. Type custom SMTP")
        smtp_choice = input("\nInput your choice (1, 2, or 3): ").strip()

        smtp_server = ""

        if smtp_choice == "1":   smtp_server = "smtp.gmail.com"
        elif smtp_choice == "2": smtp_server = "smtp-mail.outlook.com"
        else:                    smtp_server = input("\nInput custom SMTP server address: ").strip()


        app_password_path = None 
        password = None

        print("\n\nDo you already have an App password file?\n\n")



        # DO NOT HAVE USER LOOP, IF THEY FUCK UP OH WELL KICK EM OUT
        #while True:
        
        app_status = input("Yes or No: ").strip().lower()

        if app_status in ["yes", "y"]:
            app_password_path = input("Please Input path to App password file: ").strip()
        
            if os.path.exists(app_password_path):

                try:

                    with open(app_password_path, "r") as file:
                        password = file.read().strip()
                        print("Password Successfully loaded!")
                        
                except Exception as e: print(f"Error reading file: {e}. Please try again."); exit()

            else: print("File not found! Please check the path and try again."); return False


        elif app_status in ["no", "n"]: print("No password file provided."); return False
            
        else: print("Invalid input. Please type 'Yes' or 'No'"); return False

        if not password: password = input("Please manually enter your App Password: ").strip(); return False

        sender = input("\nPlease input Bot Email account: ").strip()


        if not sender: print(f"False sender"); return False


        cls._email_controller(smtp_server=smtp_server, password=password, sender=sender)





if __name__ == "__main__": 
    Email_Controller.main()