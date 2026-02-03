import os
from dotenv import load_dotenv
from langchain_classic.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from src.app.common import CustomException, logger

logger = logger.get_logger(__name__)
c_exception = CustomException.CustomException

load_dotenv()
# print(os.getenv('GROQ_API_KEY'))

class MusicClass:
    def __init__(self, temperature=0.6):
        self.llm = ChatGroq(
            temperature=temperature,
            groq_api_key=os.getenv('GROQ_API_KEY'),
            model_name='llama-3.1-8b-instant'
        )

    def generate_melody(self,user_input):
        try:
            logger.info("Generating melody notes list using LLM with the help of a prompt....!!!")
            prompt = ChatPromptTemplate.from_template("Generate a meldoy based on this input : {input}. Represented it as a space seperated notes (eg. C4 D4 E4)")
            chain = prompt | self.llm
            logger.info("Successfully created llm chain pipline with prompt for melody noted generation.....!!!")
            return chain.invoke({"input":user_input}).content.strip()
        except Exception as e:
            error_message = c_exception("Unable to create the melody notes because of the following error...",e)
            logger.error(str(error_message))
            return None
    
    def generate_harmony(self, melody):
        try:
            logger.info("Createing harmoeny from melody notes......!!!!")
            melody_prompt = ChatPromptTemplate.from_template("Create harmony chords for this melody: {melody}. Format: C4-E4-G4 F4-A4-C6")
            melody_chain = melody_prompt | self.llm
            logger.info("Successfully created harmoney melody creation llm chain pipeline for generating the musical notes accoding to the prompt....!!!!")
            return melody_chain.invoke({"melody":melody}).content.strip()
        except Exception as e:
            error_message = c_exception("Unable to create the harmoney from the melody because of the following error...",e)
            logger.error(str(error_message))
            return None
        
    def generate_rythm(self, rythm):
        try:
            logger.info("Creating beat rythm for the generated harmoney notes from medlody list......!!!!")
            rythm_prompt = ChatPromptTemplate.from_template("Suggest rhythm duration (in beats) for the following melody: {melody}. Format should be : 1.0 0.5 0.5 2.0")
            rythm_chain = rythm_prompt | self.llm
            logger.info("Successfully created the pipeline for the beat rythm generation from the harmoney using llm and prompt.....!!!!!")
            return rythm_chain.invoke({"melody":rythm}).content.strip()
        except Exception as e:
            error_message = c_exception("Unable to create the rythm from the harmony because of the following error...",e)
            logger.error(str(error_message))
            return None
        
    def adapt_style(self,style,melody,harmoney,rythm):
        try:
            logger.info("Starting to generate the mucic according to the users input style using groq....!!!!")
            style_prompt = ChatPromptTemplate.from_template(
                "Adapt to {style} style: \n Melody: {melody} \n Harmony: {Harmony} \n Rhythm: {rythm} \n Output should be in single line."
            )

            style_chain = style_prompt | self.llm

            logger.info("Successfully created the groq pipeline with adaptive prompt.....!!!!")

            return style_chain.invoke({
                "style":style,
                "melody":melody,
                "Harmony":harmoney,
                "rythm":rythm
            }).content.strip()
        except Exception as e:
            error_message = c_exception("Unable to create the music because of the following error...",e)
            logger.error(str(error_message))
            return None