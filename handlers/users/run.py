from aiogram import types
from loader import dp
import json
import time
import requests


langs = {'c': 'c', 'cpp': 'cpp', 'objectivec': 'objective-c', 'java': 'java', 'kotlin': 'kotlin', 'scala': 'scala',
         'swift': 'swift', 'csharp': 'csharp', 'go': 'go', 'haskell': 'haskell', 'erlang': 'erlang', 'perl': 'perl',
         'python': 'python3', 'ruby': 'ruby', 'php': 'php', 'bash': 'bash', 'r': 'r', 'javascript': 'javascript',
         'coffeescript': 'coffeescript', 'vb': 'vb', 'cobol': 'cobol', 'fsharp': 'fsharp', 'd': 'd',
         'clojure': 'clojure', 'elixir': 'elixir', 'mysql': 'mysql', 'rust': 'rust', 'scheme': 'scheme',
         'commonlisp': 'commonlisp', 'nadesiko': 'nadesiko', 'typescript': 'typescript', 'plain': 'plain'}
api = "http://api.paiza.io:80/runners/"


@dp.message_handler(commands=langs.keys())
async def run(message: types.Message):
    lang, code = message.text[1:message.text.find(' ')], message.text[message.text.find(' ') + 1:]
    if lang not in langs:
        lang, code = message.text[1:message.text.find('\n')], message.text[message.text.find('\n') + 1:]
    code = code.replace('>>>', '\t')
    if lang in langs.keys():
        post = requests.post(api + 'create', data={'source_code': code, 'language': langs[lang], 'api_key': 'guest'})
        request_id = json.loads(post.text)["id"]
        time_left = 1
        while True:
            time.sleep(0.005)
            time_left -= 0.005
            get = requests.get(api + 'get_status', data={'id': request_id, 'api_key': 'guest'})
            if json.loads(get.text)['status'] == 'completed':
                get = requests.get(api + 'get_details', data={'id': request_id, 'api_key': 'guest'})
                response = json.loads(get.text)
                if response['build_result'] == 'failure' or response['result'] == 'failure':
                    result = 'Error!\n' + (response["build_stderr"] if response["build_stderr"] else '') + \
                             (response["stderr"] if response["stderr"] else '')
                    break
                result = response["stdout"]
                break
            if time_left <= 0:
                result = 'Time limit exceeded :('
                break
        if result == '':
            result = 'Nothing to output :/'
        elif len(result) > 4096:
            result = 'Output is too long >_<'
        await message.answer(result)
    else:
        await message.answer('To run your script type:\n\n' + code[1:] + ' [your code]\n\nUse >>> as tabulation.')
