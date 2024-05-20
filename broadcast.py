

🌟 Bjs : var broadcast = Bot.getProperty("Broadcast") ? Bot.getProperty("Broadcast") : []

if (!broadcast.includes(user.telegramid)) {
  broadcast.push(user.telegramid)
  Bot.setProperty("Broadcast", broadcast, "json")
}

➖➖➖➖➖➖➖➖➖➖

⏩ Command : /broadcast

🌟 Bjs : var admin = Bot.getProperty("admin")

if (user.telegramid === admin) {
  var text = "*💬 Send the text for broadcast*\n\n_⚠️ Note : You can use html tags to decorate your text\n👉 Example :_ <b>Bold</b>\n                        <i>Italic</i>\n                        <u>Underline</u>\n                        <code>Mono</code>, etc."
  
  Api.sendMessage({
    text: text,
    parse_mode: "Markdown"
  })
  
  Bot.runCommand("/broadcast2")
  
} else {
  var notAdminText = "<i>⚠️ You are not admin of @" + bot.name + ".</i>"

  Api.sendMessage({
    text: notAdminText,
    parse_mode: "html"
  })
}

➖➖➖➖➖➖➖➖➖➖

⏩ Command : /broadcast2

👉 Wait for answer : On

🌟 Bjs : var admin = Bot.getProperty("admin")

if (user.telegramid === admin) {
  var broadcast = Bot.getProperty("Broadcast")

  for (var i in broadcast) {
    Api.sendMessage({
      chat_id: broadcast[i],
      text: message,
      parse_mode: "html"
    })
  }

  var text =
    "*✅ Broadcast done successfully*\n\n" + inspect(broadcast) + ""

  Api.sendMessage({
    text: text,
    parse_mode: "Markdown"
  })
} else {
  var notAdminText = "<i>⚠️ You are not admin of @" + bot.name + ".</i>"

  Api.sendMessage({
    text: notAdminText,
    parse_mode: "html"
  })
}
