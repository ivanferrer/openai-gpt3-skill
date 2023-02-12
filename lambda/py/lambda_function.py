# -*- coding: utf-8 -*-
import ask_sdk_core.utils as ask_utils
import logging
import os
import openai
from ask_sdk_core.skill_builder import SkillBuilder
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

sb = SkillBuilder()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        completions = openai.Completion.create(
            engine="text-davinci-002",
            prompt=handler_input,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5
        )
        message = completions.choices[0].text
        msg = message.strip()
        return (
            handler_input.response_builder
            .speak(msg)
            .ask(msg)
            .response
        )
