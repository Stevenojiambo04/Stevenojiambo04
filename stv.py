{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOtvIlKeGgFiXjwhvwDGLnj",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Stevenojiambo04/Stevenojiambo04/blob/main/stv.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "zMXYNzhEOXBo",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a63380bd-7b90-470b-9278-022749679b20"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Five is greater than two!\n"
          ]
        }
      ],
      "source": [
        "#This will compare 5 and 2\n",
        "if 5>2:\n",
        "  print(\"Five is greater than two!\")\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x=5\n",
        "y=3\n",
        "z=0\n",
        "print(type(x))"
      ],
      "metadata": {
        "id": "X008VMx0T0Io",
        "outputId": "bbeef0ff-b154-4618-cd28-bbde0ae62478",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'int'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#concatenation;connecting\n",
        "Full_name=print('John'+' '+'Doe')"
      ],
      "metadata": {
        "id": "4TvAfD-pV1U6",
        "outputId": "d2a487c4-b4de-45d2-ceff-06f4ad3351cc",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "John Doe\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Boolean\n",
        "Is_sunny=True\n",
        "print(type(Is_sunny))"
      ],
      "metadata": {
        "id": "ZxCU2ulFXlBR",
        "outputId": "1656200b-7aac-4570-826e-6ddc2271ff18",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'bool'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#operations in boolean\n",
        "x=True\n",
        "y=False\n",
        "print(x and y)\n",
        "print(x or y)\n",
        "print(not x)"
      ],
      "metadata": {
        "id": "zqJovTIMY1lQ",
        "outputId": "74f66ae3-8780-46dd-c016-0d797d546fcb",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n",
            "True\n",
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#variables\n",
        "x=5\n",
        "x=x+1\n",
        "print(x)"
      ],
      "metadata": {
        "id": "j368kbk3ahr8",
        "outputId": "bee11305-de02-472f-b664-d9ba7f036dce",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "6\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#operations we can perfom on variables\n",
        "#addition\n",
        "addition_output=5+3\n",
        "print(addition_output)"
      ],
      "metadata": {
        "id": "PCCvoMa3bQt0",
        "outputId": "8f6bb2ac-90a1-452e-dc17-025a788c16a2",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "8\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "ZaavA5sAe5sq"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#concatenation of string\n",
        "greeting='Hello'\n",
        "name='Alice'\n",
        "print(greeting+' '+name)"
      ],
      "metadata": {
        "id": "YImHYwwCeQzO",
        "outputId": "c591f1fa-af6f-4075-ee66-8e2db0f3b485",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello Alice\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#adding list\n",
        "list1=[1,2,3]\n",
        "list2=[4,5,6]\n",
        "print(list1+list2)"
      ],
      "metadata": {
        "id": "-ybtTKMffyoY",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "511c077b-cc06-4b52-8f99-8e2438d5e34a"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 2, 3, 4, 5, 6]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "\n",
        "#subtraction\n",
        "numbers=[1,2,3,4,5]\n",
        "numbers_remove=[3,4]\n",
        "numbers_removed=[num for num in numbers if num not in numbers_remove]\n",
        "print(numbers_removed)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rjEQ65QHgRbC",
        "outputId": "11db47c8-13d6-442a-c32e-0784d600b2f5"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 2, 5]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#repeating strings(multiply string)\n",
        "message='Hello'\n",
        "print(message*3)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "blDa8g1OgRfi",
        "outputId": "31b7995f-bf63-457e-93db-17156a00ad07"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "HelloHelloHello\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#floor division\n",
        "result=10//3\n",
        "print(result)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BWDpPYOss9hE",
        "outputId": "c4dea63b-f1b5-49d5-fcff-f1551cb6290f"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#modulus/remainder\n",
        "remainder=10%3\n",
        "print(remainder)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ign4PeE6tSxk",
        "outputId": "6c948959-23db-42e1-f7f5-742d92e24f40"
      },
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#modulus for even/odd checking\n",
        "number=10\n",
        "if number%2==0:\n",
        "  print('even')\n",
        "else:\n",
        "  print('odd')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rET8IkdQuGj5",
        "outputId": "eb7bc1d7-8acc-4211-8e12-ecac7875429e"
      },
      "execution_count": 38,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "even\n"
          ]
        }
      ]
    }
  ]
}