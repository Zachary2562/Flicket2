from application import db
from application.flicket.models.flicket_config import FlicketConfig

def main():
    # Check if a config row already exists
    if FlicketConfig.query.first():
        print("Config already exists.")
        return

    config = FlicketConfig(
        mail_server='smtp.example.com',
        mail_port=587,
        mail_use_tls=True,
        mail_use_ssl=False,
        mail_debug=False,
        mail_username='your_email@example.com',
        mail_password='your_password',
        mail_default_sender='noreply@example.com',
        mail_max_emails=10,
        mail_suppress_send=False,
        mail_ascii_attachments=False,
        posts_per_page=20,
        allowed_extensions='jpg, jpeg, png, gif',
        ticket_upload_folder='uploads/tickets',
        avatar_upload_folder='uploads/avatars',
        application_title='Recordables and TicketQuest™',
        base_url='http://localhost:5000/',
        auth_domain='',
        use_auth_domain=False,
        csv_dump_limit=1000,
        change_category=True,
        change_category_only_admin_or_super_user=True
    )
    db.session.add(config)
    db.session.commit()
    print("Default FlicketConfig created.")

if __name__ == "__main__":
    main()
