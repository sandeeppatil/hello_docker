import os
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI # Import for Gemini
from langchain_core.messages import HumanMessage # Use langchain_core.messages

# Note: The system_template remains the same as it defines the prompt structure.
system_template = """
Original Word:
{word}

Root Word (Grundform):
# For verbs: the infinitive (e.g., "schlafen" for "schlafe").
# For nouns: the singular nominative form with its definite article (e.g., "der Baum" for "Bäume").
# For adjectives: the uninflected positive form (e.g., "schön" for "schönen").
# For other word types: state "N/A" or briefly explain why a root form isn't applicable (e.g., for adverbs, prepositions, which often don't have a distinct "root" in the same sense).

English Meaning:
# The primary English translation(s) of the root word

Word Type (Wortart):
# The grammatical part of speech (e.g., Nomen, Verb, Adjektiv, Adverb, Präposition, Pronomen, Konjunktion, Interjektion)

Grammatical Forms:
# Present the various forms of the word in a Markdown table.
# If the word is inflectable (e.g., Noun, Verb, Adjective, Pronoun, Article):
# Create a table with columns appropriate for its inflection.
# For Verbs: Include columns for Person, Number, Tense (e.g., Präsens, Präteritum, Perfekt), and Mood (e.g., Indikativ, Konjunktiv I, Imperativ). Include relevant irregular forms (e.g., past participle).
# For Nouns: Include columns for Case (Nominativ, Genitiv, Dativ, Akkusativ), Number (Singular, Plural), and Definite Article. Clearly state the gender of the noun.
# For Adjectives: Include columns for Comparison (Positive, Komparativ, Superlativ) and, if applicable, Declension (e.g., Strong, Weak, Mixed) with example articles/nouns if necessary to illustrate.
# For Pronouns/Articles: Include columns for Case, Number, and Gender.
# If the word is uninflectable (e.g., most Adverbs, Prepositions, Conjunctions, Interjections):
# State clearly: "This word is uninflectable and does not change form."

Example Sentence & Translation:
# German Sentence: One simple, clear example sentence using the original word provided by the user.
# English Translation: The accurate English translation of the example sentence.
"""

def get_gemini_api_key():
    """Get the GOOGLE_API_KEY environment variable."""
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        return None
    return api_key

def main():
    st.title("German Word Analysis App")
    api_key = get_gemini_api_key()

    if not api_key:
        st.write("⚠️ Please set the **GOOGLE_API_KEY** environment variable.")
        st.markdown("You can get a free API key from [Google AI Studio](https://aistudio.google.com/app/apikey).")
        return

    word = st.text_input("Enter a German word for grammatical analysis:")

    if word:
        if len(word.split()) > 1:
            st.write("⚠️ Please enter a single word.")
            return

        st.write(f"You entered: **{word}**")

        try:
            # Initialize the Gemini model
            # You can choose different models like "gemini-pro", "gemini-1.5-flash", etc.
            # "gemini-pro" is a good general-purpose choice.
            model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=api_key)

            # Create the PromptTemplate instance
            german_grammar_prompt = PromptTemplate(
                input_variables=["word"],
                template=system_template
            )

            formatted_prompt = german_grammar_prompt.format(word=word)

            # Send the prompt to the Gemini model
            # Note: For Chat models, you typically send a list of messages.
            # Here, we send our formatted prompt as a HumanMessage.
            response = model.invoke([HumanMessage(content=formatted_prompt)])

            if response.content: # Access the response content
                st.markdown(response.content)
            else:
                st.write("⚠️ No response generated from the model.")

        except Exception as e:
            # Generic error handling; you might want more specific handling for Gemini API errors
            st.write(f"❌ An error occurred: {e}")
            st.write("Please ensure your **GOOGLE_API_KEY** is correct and you have enough quota.")

if __name__ == "__main__":
    main()