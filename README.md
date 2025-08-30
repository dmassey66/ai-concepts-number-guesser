# AI Number Guesser — Reasoning Agent Concepts

Project 1.   Number guessing.  , A “number guessing game” in Python feels like just a toy project, but if you zoom out, it actually touches the roots of how reasoning in AI works.
----------------------------------------------------------------------------------------------------------------
🔹 1.** The Classic Number Guessing Game**
      •	You (the human) think of a number.
      •	The program asks questions or makes guesses.
      •	Based on your feedback (“too high,” “too low”), it adjusts until it finds the right number.
        This is basically a search problem.
________________________________________
🔹 2.** Where AI Reasoning Shows Up**
      1.	Search and Inference
        o	The program doesn’t know the answer at first.
        o	It has to reason by elimination, shrinking the possible solution space each time.
        o	That’s the same core principle as how AI narrows down likely answers in reasoning tasks.
      2.	Hypothesis Testing
        o	Each guess is like a hypothesis (“I think the number is 50”).
        o	Feedback from the human (“too high”) is evidence.
        o	The program updates its belief and forms a new hypothesis.
        o	This mirrors Bayesian reasoning and logical deduction in AI.
      3.	Optimization
        o	If the program just guesses randomly, it might take forever.
        o	A smarter strategy (like binary search) finds the answer in the fewest steps.
        o	That’s essentially an optimization problem — a cornerstone of AI reasoning.
________________________________________
🔹 3. **The Bigger AI Connection**
      •	The game is a mini model of reasoning under uncertainty: the program starts ignorant, gathers feedback, eliminates wrong paths, and converges on the truth.
      •	Replace “numbers” with “diagnoses,” “strategies,” or “predictions,” and you’ve got the same reasoning pattern AI uses in medicine, cybersecurity, or even stock trading.
      •	In fact, the same logic behind guessing your number is behind decision trees, constraint satisfaction problems, and search-based AI planning.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**What it does:** Guesses a number using feedback, higher/lower.  
            
## How to run
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
streamlit run app/main.py
```

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dmassey66/ai-number-guesser/blob/main/notebooks/demo.ipynb)




