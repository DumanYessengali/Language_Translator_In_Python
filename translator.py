import requests
import sys

from bs4 import BeautifulSoup


class Translator:
    def __init__(self):
        args = sys.argv
        self.lang1 = args[1]
        self.lang2 = args[2]
        self.wordTrans = args[3]
        self.languages = {
            1: 'arabic',
            2: 'german',
            3: 'english',
            4: 'spanish',
            5: 'french',
            6: 'hebrew',
            7: 'japanese',
            8: 'dutch',
            9: 'polish',
            10: 'portuguese',
            11: 'romanian',
            12: 'russian',
            13: 'turkish'
        }

    def mainFunction(self):
        if self.lang2 in self.languages.values():
            link = f'https://context.reverso.net/translation/{self.lang1}-{self.lang2}/' + self.wordTrans
            user_agent = 'Mozilla/5.0'
            try:
                r = requests.get(link, headers={'User-Agent': user_agent})
                r.raise_for_status()
            except requests.exceptions.ConnectionError as errc:
                print('Something wrong with your internet connection')
            except requests.exceptions.HTTPError as err:
                print(f"Sorry, unable to find {self.wordTrans}")
            else:
                file = open(f'{self.wordTrans}.txt', 'x', encoding='utf-8')
                print(f"{self.lang2.capitalize()} Translations:")
                file.write(f"{self.lang2.capitalize()} Translations:")
                file.close()
                soup = BeautifulSoup(r.content, 'html.parser')

                a_word = soup.find_all(id='translations-content')
                array1 = a_word[0].text.replace('\n', '').split('          ')
                array1.remove('')
                n = 0
                if len(array1) > 5:
                    array1 = array1[0:5]
                file = open(f'{self.wordTrans}.txt', 'a', encoding='utf-8')
                for i in array1:
                    print(i)
                    file.write('\n' + i)
                examples = []
                print(f'\n{self.lang2.capitalize()} Examples:')
                file.write(f'\n\n{self.lang2.capitalize()} Examples:\n')
                for item in soup.find_all('div', {'class': ['src', 'trg']}):
                    examples.append(item.text.strip())
                examples = list(filter(None, examples))
                if len(examples) > 10:
                    print("\n\n".join(("\n".join(j for j in examples[i:i + 2]) for i in range(0, 10, 2))))
                    file.write("\n\n".join(("\n".join(j for j in examples[i:i + 2]) for i in range(0, 10, 2))))
                else:
                    print("\n\n".join(("\n".join(j for j in examples[i:i + 2]) for i in range(0, len(examples), 2))))
                    file.write("\n\n".join(("\n".join(j for j in examples[i:i + 2]) for i in range(0, len(examples), 2))))
                file.close()
        elif self.lang2 == "all":
            file = open(f'{self.wordTrans}.txt', 'x', encoding='utf-8')
            for j in self.languages:
                link = f'https://context.reverso.net/translation/{self.lang1}-{self.languages[int(j)]}/' + self.wordTrans
                user_agent = 'Mozilla/5.0'
                try:
                    r = requests.get(link, headers={'User-Agent': user_agent})
                    r.raise_for_status()
                except requests.exceptions.ConnectionError as errc:
                    print('Something wrong with your internet connection')
                except requests.exceptions.HTTPError as err:
                    print(f"Sorry, unable to find {self.wordTrans}")
                    break
                else:
                    if self.languages[int(j)] == self.lang1:
                        continue
                    file = open(f'{self.wordTrans}.txt', 'a', encoding='utf-8')
                    print(f"{self.languages[int(j)].capitalize()} Translations:")
                    file.write(f"{self.languages[int(j)].capitalize()} Translations:")
                    file.close()
                    soup = BeautifulSoup(r.content, 'html.parser')
                    a_word = soup.find_all(id='translations-content')
                    array1 = a_word[0].text.replace('\n', '').split('          ')
                    array1.remove('')
                    n = 0
                    if len(array1) > 1:
                        array1 = array1[0:1]
                    file = open(f'{self.wordTrans}.txt', 'a', encoding='utf-8')
                    for i in array1:
                        print(i)
                        file.write('\n' + i)
                    examples = []
                    print(f'\n{self.languages[int(j)].capitalize()} Examples:')
                    file.write(f'\n\n{self.languages[int(j)].capitalize()} Examples:\n')
                    for item in soup.find_all('div', {'class': ['src', 'trg']}):
                        examples.append(item.text.strip())
                    examples = list(filter(None, examples))
                    print("\n\n".join(("\n".join(j for j in examples[i:i + 2]) for i in range(0, 2, 2))))
                    file.write("\n\n".join(("\n".join(j for j in examples[i:i + 2]) for i in range(0, 2, 2))))
                    print("\n")
                    file.write("\n\n\n")
                    file.close()
        else:
            print(f"Sorry, the program doesn't support {self.lang2}")



if __name__ == '__main__':
    Translator().mainFunction()