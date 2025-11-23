import pywhatkit as kit

def send_whatsapp_message(phone_number, message):
    """
    Send a WhatsApp message using pywhatkit.
    Note: This requires WhatsApp Web to be open and logged in.
    phone_number should be in international format, e.g., +1234567890
    """
    try:
        # Validate phone number format
        if not phone_number.startswith('+'):
            phone_number = '+' + phone_number

        # Send message instantly (requires WhatsApp Web to be open)
        kit.sendwhatmsg_instantly(phone_number, message, wait_time=10, tab_close=True)
        print(f"WhatsApp message sent to {phone_number}: {message}")
        return True
    except Exception as e:
        print(f"Error sending WhatsApp message: {e}")
        return False
