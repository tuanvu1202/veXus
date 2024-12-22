for file in os.listdir("modules/commands"):
    if file.endswith(".py"):
        try:
            try:
                await self.bot.load_extension(f"modules.commands.{file[:-3]}")
                if file in configValue["commandDisabled"]:
                    configValue["commandDisabled"].remove(file) 
                    logger(f"Load thành công {file}", "load")
                    commandSuccess+=1
            except commands.ExtensionAlreadyLoaded:
                try:
                    await self.bot.reload_extension(f"modules.commands.{file[:-3]}")
                    if file in configValue["commandDisabled"]:
                        configValue["commandDisabled"].remove(file) 
                        logger(f"Load thành công {file}", "load")
                        commandSuccess+=1
                except Exception as e:
                    await ctx.send(e)
        except Exception as e:
            logger(f"Load không được {file}", "error")
            await ctx.send(e)
            commandFailed+=1
            
            
await ctx.send(f"Load thành công {commandSuccess} lệnh và thất bại {commandFailed} lệnh!")
