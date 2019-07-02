from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler


class SelfEsteemSkill(MycroftSkill):

    def __init__(self):
        super(SelfEsteemSkill, self).__init__(name="SelfEsteemSkill")

    @intent_handler(IntentBuilder("BeautifulIntent").require("Beautiful").optional("pronoun"))
    def handle_beautiful_intent(self, message):
        self.speak_dialog("you.are.beautiful")

    @intent_handler(IntentBuilder("SmartIntent").require("Smart").optional("pronoun"))
    def handle_smart_intent(self, message):
        self.speak_dialog("you.are.smart")

    @intent_handler(IntentBuilder("StupidIntent").require("Smart").optional("pronoun"))
    def handle_stupid_intent(self, message):
        self.speak_dialog("of.course.not")
        self.speak_dialog("you.are.smart")


def create_skill():
    return SelfEsteemSkill()
