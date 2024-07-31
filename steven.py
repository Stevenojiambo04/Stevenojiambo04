{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMxvy+GoUoE15JtirN8tyaR",
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
        "<a href=\"https://colab.research.google.com/github/Stevenojiambo04/Stevenojiambo04/blob/main/steven.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
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
      "execution_count": null,
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
      "execution_count": null,
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
      "execution_count": null,
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
      "execution_count": null,
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
      "execution_count": null,
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
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "even\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#logical operations(and, or, not)\n",
        "a=5\n",
        "b=10\n",
        "c=15\n",
        "result=not(a<b and b<c)and(a<c)\n",
        "print(result)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LhtnOfoN_S8-",
        "outputId": "9e88dc7b-2c7a-44fd-a689-a6535be33385"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#comparision operators\n",
        "x=20\n",
        "y=15\n",
        "print(x==y)\n",
        "print(x!=y)\n",
        "print(x>y)\n",
        "print(x<y)\n",
        "print(x>=y)\n",
        "print(x<=y)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "g-un_12FBRKn",
        "outputId": "3eef9135-cd03-4292-ee85-4b67d7a19f3b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n",
            "True\n",
            "True\n",
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
        "x='apple'\n",
        "y='banana'\n",
        "if x<y:\n",
        "  print(\"x is greater than y\")\n",
        "else:\n",
        "   print(\"y is greater than x\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sloj0PgIB4sO",
        "outputId": "1d03c714-1f16-4b53-9290-684d81b3fe25"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "x is greater than y\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "result=print(3<5>7)\n",
        "result=print(3<5<7)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MQ-XfE-xDmk5",
        "outputId": "9fdca460-8f0c-41c1-8d56-93240817d056"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n",
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#bitwise\n",
        "a=5\n",
        "b=3\n",
        "print(a&b)\n",
        "print(a|b)\n",
        "print(a^b)\n",
        "print(~a)\n",
        "print(a<<2)\n",
        "print(a>>2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_T4JTIn-FPBa",
        "outputId": "8b5305c8-51f1-46c7-d5d3-de6b8fb7d43b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "7\n",
            "6\n",
            "-6\n",
            "20\n",
            "1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#membership operation\n",
        "list=[1,2,3,4,5]\n",
        "print(3 in list)\n",
        "print(6 not in list)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WjMk1PrKGKvL",
        "outputId": "d6923f85-4a2d-4051-c6ff-c201811e282a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n",
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#slicing (string) in python\n",
        "message='Helloworld!'\n",
        "print(message[0:5])\n",
        "print(message[7:])\n",
        "print(message[:5])\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IcYvxKYzIT-0",
        "outputId": "559591a0-c161-492e-ddd3-5af9a14c92a7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello\n",
            "rld!\n",
            "Hello\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#compression methods\n",
        "#insert\n",
        "fruits=['apple','banana','cherry',]\n",
        "fruits.insert(1,'blueberry')\n",
        "print(fruits)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3Pc6MkstJpOv",
        "outputId": "a7d99983-6732-4121-f6cb-12b681896c1e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['apple', 'blueberry', 'banana', 'cherry']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#remove\n",
        "fruits=['apple','banana','cherry']\n",
        "fruits.remove('banana')\n",
        "print(fruits)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_ovX0rOVIUDv",
        "outputId": "ba43869f-4acd-4415-cfea-a3b7d9d3bc2f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['apple', 'cherry']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#pop\n",
        "fruits=['apple','banana','cherry']\n",
        "fruits.pop(2)\n",
        "print(fruits)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6Xjdv31vIUVR",
        "outputId": "59927b42-85af-494c-dbc7-290cc71fbeec"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['apple', 'banana']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#tuple\n",
        "this_tuple=('apple','banana','cherry')\n",
        "print(this_tuple)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NLgBr_GINaQh",
        "outputId": "28aef4d4-c3fa-48c0-d42b-43cdd764d80f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "('apple', 'banana', 'cherry')\n"
          ]
        }
      ]
    }
  ]
}