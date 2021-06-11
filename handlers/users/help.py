from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Command list: ",
            "/help - Get help",
            "/c [code] - Run c script",
            "/cpp [code] - Run cpp script",
            "/objectivec [code] - Run objectivec script",
            "/java [code] - Run java script",
            "/kotlin [code] - Run kotlin script",
            "/scala [code] - Run scala script",
            "/swift [code] - Run swift script",
            "/csharp [code] - Run csharp script",
            "/go [code] - Run go script",
            "/haskell [code] - Run haskell script",
            "/erlang [code] - Run erlang script",
            "/perl [code] - Run perl script",
            "/python [code] - Run python script",
            "/ruby [code] - Run ruby script",
            "/php [code] - Run php script",
            "/bash [code] - Run bash script",
            "/r [code] - Run r script",
            "/javascript [code] - Run javascript script",
            "/coffeescript [code] - Run coffeescript script",
            "/vb [code] - Run vb script",
            "/cobol [code] - Run cobol script",
            "/fsharp [code] - Run fsharp script",
            "/d [code] - Run d script",
            "/clojure [code] - Run clojure script",
            "/elixir [code] - Run elixir script",
            "/mysql [code] - Run mysql script",
            "/rust [code] - Run rust script",
            "/scheme [code] - Run scheme script",
            "/commonlisp [code] - Run commonlisp script",
            "/nadesiko [code] - Run nadesiko script",
            "/typescript [code] - Run typescript script",
            "/plain [code] - Run plain script")
    
    await message.answer("\n".join(text))
