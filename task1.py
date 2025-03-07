{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Multiplication result: 24\n"
     ]
    }
   ],
   "source": [
    "\n",
    "from functools import reduce\n",
    "\n",
    "def multiply_numbers(numbers):\n",
    "    return reduce(lambda x, y: x * y, numbers)\n",
    "\n",
    "numbers = [2, 3, 4]\n",
    "result = multiply_numbers(numbers)\n",
    "print(f\"Multiplication result: {result}\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
