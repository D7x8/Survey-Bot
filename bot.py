from splinter import Browser
browser = Browser()

target = input("Enter the targeted survey from Rewardia.com: ")

browser.visit(target)

print(browser.html)