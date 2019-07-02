from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler

# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.


class SelfEsteemSkill(MycroftSkill):

    @intent_handler(IntentBuilder("BeautifulIntent").require("Beautiful").require("pronoun"))
    def handle_beautiful_intent(self, message):
        if message.data["pronoun"] == "i":
            self.speak_dialog("you.are.beautiful")

    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, there is no need to override it.  If you DO
    # need to implement stop, you should return True to indicate you handled
    # it.
    #
    # def stop(self):
    #    return False


def create_skill():
    return SelfEsteemSkill()
