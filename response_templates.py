"""
Response templates for the travel engagement bot.
This file contains various response templates organized by destination/topic.
"""

import os
from huggingface_hub import InferenceClient
import requests

# Get Hugging Face token from environment
HF_TOKEN = os.getenv('HF_TOKEN')
if HF_TOKEN:
    # Using Qwen 2.5 7B as the primary model - good balance of quality and speed
    HF_MODEL = os.getenv('HF_MODEL', 'Qwen/Qwen2.5-7B-Instruct')
    client = InferenceClient(token=HF_TOKEN, model=HF_MODEL)
    HF_ENABLED = True
else:
    HF_ENABLED = False
    print("Warning: HF_TOKEN not found in environment variables. Hugging Face integration disabled.")
    client = None
    HF_MODEL = None

# Generic response templates
GENERIC_RESPONSES = [
    "That's a great question! Based on my experience, here are some thoughts...",
    "Hey there! I've been to that destination and can definitely help. Here's what I recommend...",
    "I had a similar question recently and learned a lot about this. Here's what helped me...",
    "Great topic! Here are some tips that might be helpful for your situation...",
    "Based on what you're looking for, I'd suggest...",
    "I've heard this question come up a lot. Here's what I usually tell people in your situation...",
    "Wonderful destination choice! Based on what I know, here are some ideas...",
    "I love helping people plan trips! Here's what I've learned about your particular situation...",
    "From my experience with similar trips, here are some key points to consider...",
    "Excellent question! Here's what I think would work well for you..."
]

# Tokyo-specific responses
TOKYO_RESPONSES = [
    "Tokyo is incredible but definitely overwhelming! Here's a solid 5-day breakdown:\n\n"
    "Day 1: Shibuya/Harajuku (hit the famous crossing, explore Takeshita Street)\n"
    "Day 2: Asakusa/Skytree (traditional temple vibes + modern views)\n"
    "Day 3: Akihabara/Ueno (anime/tech heaven + museums)\n"
    "Day 4: Day trip to Nikko or Kamakura\n"
    "Day 5: Tsukiji Market morning + Ginza shopping\n\n"
    "Pro tip: Get a Suica card first thing—makes train travel so much easier.\n\n"
    "If you want, I can create a visual itinerary that maps this out in a more fun way than a boring list. "
    "I've been making these crayon-style travel journals that people seem to enjoy. "
    "Happy to make one for your Tokyo trip if you'd like to see what it looks like!",

    "Tokyo can be intimidating for first-timers, but it's absolutely magical! A few highlights:\n\n"
    "- The train system is your friend - download the Google Translate app for station announcements\n"
    "- Don't miss the early morning Tsukiji tuna auction if it's still happening during your visit\n"
    "- Take time to explore neighborhoods beyond the tourist areas like Yanaka\n"
    "- For food, try the department store basements - they're like food paradises!\n\n"
    "I specialize in creating visual travel plans that make navigating Tokyo easier. "
    "Would love to help create a personalized guide for your trip!"
]

# Paris-specific responses
PARIS_RESPONSES = [
    "Oh, the food in Paris is unreal! Some favorites:\n\n"
    "• L'As du Fallafel (Marais) - best falafel outside Israel\n"
    "• Marché des Enfants Rouges - oldest covered market, amazing lunch spots\n"
    "• Breizh Café - incredible crêpes in the Marais\n"
    "• Any random boulangerie for croissants (seriously, they're all good)\n\n"
    "Don't sleep on the neighborhood bistros—sometimes the best meals are the unplanned ones where you just wander in.\n\n"
    "Are you planning a full Paris trip? I love helping visualize itineraries if you need help mapping out your days!",

    "Paris is all about savoring the moment! Here are some non-obvious tips:\n\n"
    "• Many museums are closed on Mondays - plan accordingly\n"
    "• Visit Montmartre early morning to beat the crowds\n"
    "• The promenade along the Seine has hidden gems - walk the full length\n"
    "• For authentic experiences, eat dinner later like locals do (after 8pm)\n\n"
    "I create these visual travel journals in a crayon style that make planning more enjoyable. "
    "If you'd like, I could draft a visual itinerary for your Paris trip!"
]

# Japan general responses
JAPAN_RESPONSES = [
    "Japan is such an amazing country with unique customs! Here are some key things to know:\n\n"
    "• Bow instead of handshake when greeting someone\n"
    "• Slurping noodles is a sign of appreciation\n"
    "• Tipping isn't customary and can be offensive\n"
    "• Shoes come off indoors in homes and some restaurants\n"
    "• Vending machines everywhere - even in remote locations!\n\n"
    "I've been helping travelers plan Japan trips with visual itineraries. "
    "Would you like me to create a personalized travel journal for your Japan adventure?",
    
    "One of the best aspects of Japan is the efficiency of everything! Some transportation tips:\n\n"
    "• Get a Japan Rail Pass before arrival if you're traveling between cities\n"
    "• Download Hyperdia or Japan Transit Planner for train schedules\n"
    "• Suica/PASMO cards work on most city transportation\n"
    "• Trains are punctual to the minute - be on time!\n\n"
    "Creating a visual plan can make your Japan experience even smoother. "
    "I specialize in crayon-style travel journals that make trip planning more engaging!"
]

# Europe/General travel responses
EUROPE_RESPONSES = [
    "European travel has some great money-saving tips! Here are essentials:\n\n"
    "• Get a rail pass if traveling between countries\n"
    "• Many museums offer free admission days\n"
    "• Shop at local markets for budget-friendly meals\n"
    "• City tourist cards often provide good value for attractions\n"
    "• Book accommodations in advance during peak season\n\n"
    "I create personalized visual travel plans that can make your European adventure more organized. "
    "Would a crayon-style travel journal help with your planning?", 
    
    "Europe has such diverse cultures packed into a compact area! My top tips:\n\n"
    "• Learn basic greetings in local languages\n"
    "• Pack light - luggage on cobblestones is difficult\n"
    "• Evening meals are later in Southern Europe\n"
    "• Tipping customs vary significantly between countries\n"
    "• Many sites are closed on Sundays/Mondays\n\n"
    "I've been making visual trip planners that people find really helpful. "
    "Would love to create one for your European trip!"
]

# Southeast Asia responses
SEA_RESPONSES = [
    "Southeast Asia is such an incredible region for culture and value! Here's what I recommend:\n\n"
    "• Pack light - clothes dry quickly in the humidity\n"
    "• Stay in locally-owned guesthouses for authentic experiences\n"
    "• Eat street food - it's often the safest and tastiest option\n"
    "• Negotiate tuk-tuk fares upfront\n"
    "• Respect temple dress codes (covered shoulders/knees)\n\n"
    "Visual planning can be super helpful in Southeast Asia. "
    "I create these fun, crayon-style travel journals that help keep track of all the amazing places to visit!",

    "The diversity within Southeast Asia is mind-blowing! Some unique insights:\n\n"
    "• Bargain respectfully at markets (it's expected!)\n"
    "• Mosquito protection is essential, especially during rainy season\n"
    "• Transportation varies dramatically between countries\n"
    "• Tipping etiquette differs by country\n"
    "• Many credit cards charge foreign transaction fees\n\n"
    "If you'd like, I can create a personalized travel journal for your Southeast Asia adventure!"
]

# Solo travel responses
SOLO_TRAVEL_RESPONSES = [
    "Solo travel is such a rewarding experience! Here are key tips I always share:\n\n"
    "• Choose accommodations with communal spaces to meet fellow travelers\n"
    "• Join free walking tours to connect with others\n"
    "• Eat at counters instead of tables for spontaneous conversations\n"
    "• Consider solo dining during restaurant hours to avoid awkwardness\n"
    "• Research female-friendly resources if traveling as a woman\n\n"
    "I create travel journals that can make solo trips feel less lonely. "
    "My crayon-style planner helps keep you connected to your purpose for traveling alone!",

    "The freedom of solo travel comes with some unique considerations:\n\n"
    "• Share your location with someone back home regularly\n"
    "• Take advantage of being able to change plans spontaneously\n"
    "• Trust your instincts - if something feels off, remove yourself\n"
    "• Embrace activities you might not do with others (theater alone, anyone?)\n"
    "• Document your journey extensively - you'll cherish these memories\n\n"
    "Would a personalized travel journal help organize your solo adventure thoughts? "
    "I specialize in visual planners that make solo travel more meaningful!"
]

def generate_contextual_response(comment_text, subreddit_name, additional_context=None):
    """
    Generate a contextual response using Hugging Face model based on the comment and subreddit.
    """
    if not HF_ENABLED:
        # Fallback to rule-based responses if HF is not enabled
        return get_destination_specific_response(comment_text)

    # Base context for travel advice
    base_context = f"""
    You are a helpful travel advisor named Travel Planning Enthusiast (username: crayontravel_helper).
    You create hand-drawn style travel journals and share travel planning tips.
    """

    # Add additional context if provided
    if additional_context:
        base_context += f"\nAdditional Context: {additional_context}\n"

    # Craft a prompt for the model based on the comment
    prompt = f"""
{base_context}
A Reddit user in r/{subreddit_name} asked: "{comment_text}"

Provide helpful, friendly travel advice that addresses their question directly.
Keep responses concise but informative (2-3 paragraphs max).
At the end, naturally mention that you create crayon-style travel journals if relevant to their query,
but only if it fits naturally and adds value.
Use a friendly, knowledgeable tone.

Response:
"""

    try:
        # Generate response using Hugging Face model
        response = client.text_generation(
            prompt,
            max_new_tokens=300,
            temperature=0.7,
            do_sample=True,
            stop_sequences=["\n\n", "User:", "Comment:", "A Reddit user"]
        )

        # Clean up the response
        # The response might contain the prompt, so we extract just the generated part
        if "Response:" in response:
            response = response.split("Response:")[-1].strip()
        elif "A Reddit user" in response:
            # If it echoed the prompt, take everything after
            parts = response.split("A Reddit user")
            if len(parts) > 1:
                response = parts[0].strip()

        return response
    except Exception as e:
        print(f"Error generating response with Hugging Face: {e}")
        # Fallback to rule-based response
        return get_destination_specific_response(comment_text) or random.choice(GENERIC_RESPONSES)


def load_context_from_file(file_path):
    """
    Load specific context from a file to be used in responses.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Context file {file_path} not found.")
        return None
    except Exception as e:
        print(f"Error reading context file: {e}")
        return None


def save_context_to_file(context, file_path):
    """
    Save context to a file for future use.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(context)
        print(f"Context saved to {file_path}")
    except Exception as e:
        print(f"Error saving context: {e}")


def get_destination_specific_response(comment_text):
    """
    Returns a destination-specific response based on keywords in the comment.
    This serves as a fallback when Hugging Face is not available.
    """
    comment_lower = comment_text.lower()

    # Tokyo/Japan related
    if 'tokyo' in comment_lower:
        import random
        return random.choice(TOKYO_RESPONSES)
    elif 'japan' in comment_lower or 'kyoto' in comment_lower or 'osaka' in comment_lower:
        import random
        return random.choice(JAPAN_RESPONSES)
    elif 'paris' in comment_lower:
        import random
        return random.choice(PARIS_RESPONSES)
    elif ('europe' in comment_lower and ('trip' in comment_lower or 'travelling' in comment_lower or 'vacation' in comment_lower)) or 'european' in comment_lower:
        import random
        return random.choice(EUROPE_RESPONSES)
    elif any(place in comment_lower for place in ['thailand', 'bali', 'vietnam', 'cambodia', 'malaysia', 'indonesia']):
        import random
        return random.choice(SEA_RESPONSES)
    elif 'solo' in comment_lower and ('travel' in comment_lower or 'trip' in comment_lower):
        import random
        return random.choice(SOLO_TRAVEL_RESPONSES)

    return None