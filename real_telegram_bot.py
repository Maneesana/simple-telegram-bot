from ast import Call
from email import message
from telegram import ReplyKeyboardMarkup, Update
import telegram
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)
from datetime import datetime
from datetime import timedelta
import logging

accessToken='5230562427:AAE5yDe9IYD4-5lk33z6k2bU6422ytrl9Qo'

logging.basicConfig(level=logging.INFO,format="%(asctime)s --- %(name)s --- %(levelname)s --- %(message)s ")

updater=Updater(token=accessToken,use_context=True)
dp=updater.dispatcher


# command -- /start
welcome_text='''
|=====WELCOME TO=====| 
CHEAP STORE PREMIUM SHOP
Powered by : Chingnung Laija Erik Bot
A bot created by: @Naphan792
~~~~~~~~~~~~~~~~~~~~~~~~~
🌸🌺🌼💮🌻🌷💑💕💦💥
>>> /start - to start bot 
>>> /createInvoice - to create invoice (admin)
>>> /stop -- stop conversation
💦💥💤🌸🌺🌼💮🌻🌷💑
~~~~~~~~~~~~~~~~~~~~~~~~~

'''

def start(update:Update,context:CallbackContext):
    update.message.reply_text(welcome_text)
cmd_start_handler=CommandHandler("start",start)
dp.add_handler(cmd_start_handler)










# command --/createInvoice

from telegram import ReplyKeyboardMarkup,ReplyKeyboardRemove
from uuid import uuid4

#only admin priviledge
# bot=telegram.Bot(token=accessToken)





def createInvoice(update:Update,context:CallbackContext):
    update.message.reply_text("Are you Admin or a customer?",reply_markup=ReplyKeyboardMarkup(reply_array,one_time_keyboard=True,input_field_placeholder="admin or customer"))
    
    


invoice_cmd=CommandHandler("createInvoice",createInvoice)
dp.add_handler(invoice_cmd)
    




def calcValid():
    return (today+timedelta(days=30)).strftime("%d-%b-%Y")

global today
today=datetime.now()

print("Today is :"+today.strftime("%d-%b-%Y"))
# global userName,userChatID,userTransactionID,userAmount,userCode

validityDate=calcValid()
channelLink='https://t.me/+RbWgIVBIWg41MTFl'

    




reply_array=[["/Admin 🎯","/Customer 🧸"]]
def adminUser(update:Update,context:CallbackContext):
    adminUserName='Naphan792'
    print("You are calling")
    userName=update.message.from_user.username
 
    if(update.message.text == reply_array[0][0]):
        print("Admin selected")
        if(userName==adminUserName):
            print("Booss")
            update.message.reply_text("Yes,Boss Hello Maibam Maneesana")
    
            #update chatID
            context.user_data["chat"]=update.message.chat.id
            update.message.reply_text("Use /name- 'value' to enter name :")

            
           
           
            
       
            
            


        else:
            update.message.reply_text("You lied to me you are not my boss")            
        
def getAmount(update:Update,context:CallbackContext):
    value = update.message.text.partition(' ')[2]
    context.user_data["amount"]=value   
    update.message.reply_text("Use /tran 'value'\n Enter user transaction ID: ")

def nameproduct(update:Update,context:CallbackContext):
    value = update.message.text.partition(' ')[2]
    context.user_data["product-name"]=value   
    update.message.reply_text("Use /amt 'your value' -to give value!\nEnter amount paid by user: ")




def getTransactionID(update:Update,context=CallbackContext):
    value = update.message.text.partition(' ')[2]
    context.user_data["transaction"]=value
    update.message.reply_text("Use /gen- to Generate user Code")

def getName(update:Update,context=CallbackContext):
    value = update.message.text.partition(' ')[2]
    context.user_data["user-name"]=value
    update.message.reply_text("Use /prod 'value'\n Enter product name: ")         
    
def genCode(update:Update,context=CallbackContext):
    
    context.user_data["code"]=str(uuid4()).upper()
    data=context.user_data
    invoiceContent=f'''
|============RECIEPT==========|
# User Name🧑🏻:{data.get("user-name")} \t\t\t\t\t#
# Chat_id: {data.get("chat")} \t\t\t\t\t\t#
# Product Name: {data.get("product-name")} \t\t\t\t\t\t#
# Amount paid 💲: Rs.{data.get("amount")}\t\t\t\t\t#
# Date: {today.strftime("%d-%b-%Y")} \t\t\t\t\t\t#
# Transaction_ID: {data.get("transaction")}\t\t\t\t\t\t#
# Valid Upto: {validityDate} \t\t\t\t\t#
# Your Unique CODE: {data.get("code","not found")} \t\t\t#
# Thank you for shopping 🛒💳 with Cheap Store Premium \t\t#
# Pls support our channel \t\t\t\t\t#
# Pls subscribe our channel🌐: {channelLink}\t#
# |###########################---END---############################|
 '''

    
    update.message.reply_text("You have sucessfully created your invoice!!")
    update.message.reply_text(f"YOUR INVOICE GENERATED : \n{invoiceContent}")


dp.add_handler(CommandHandler("amt",getAmount))
dp.add_handler(CommandHandler("tran",getTransactionID))
dp.add_handler(CommandHandler("gen",genCode))
dp.add_handler(CommandHandler("name",getName))
dp.add_handler(CommandHandler("prod",nameproduct))
admin_cmd=CommandHandler("Admin",adminUser)
dp.add_handler(admin_cmd)

def stop(update:Update,context:CallbackContext):
    update.message.reply_text("Bye!Bye! Have a great time. To start again use - /start")
    update.message.reply_text("Thank you for using ~ ChingnungLaijaErikBot")
    ConversationHandler.END
def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

def customer(update: Update, context: CallbackContext):
    update.message.reply_text("You don't have the right priviledge to opt this feature")






dp.add_handler(CommandHandler("Customer",customer))

dp.add_handler(CommandHandler("stop",stop))
unknown_handler = MessageHandler(Filters.command, unknown)
dp.add_handler(unknown_handler)
# command --/generate-code
#main function starts here
updater.start_polling()
updater.idle()
