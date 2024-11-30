from app.utils.flash_message_category import FlashMessageCategory


class FlashMessage:
  def __init__(self, message, alertType, category: FlashMessageCategory = None):
    self.message = message
    self.alertType = alertType
    self.category = category