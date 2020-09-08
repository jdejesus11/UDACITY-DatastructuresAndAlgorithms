from RequestRouting import Router

router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler") 
router.add_handler("/home/prices", "about prices") 
router.add_handler("/home/products", "about products") 
router.add_handler("/home/products/1234/details", "about 1234 details") 

def print_test(test_name,router,path):
    print(test_name)
    handler_name = router.lookup(path)
    print("The handler for {} is: {}".format(path,handler_name))
    print("")

print_test("Test #1: ",router,"/")

print_test("Test #2: ",router,"home")

print_test("Test #3: ",router,"/home/")

print_test("Test #4: ",router,"/home/about")

print_test("Test #5: ",router,"/home/about/me/")

print_test("Test #6: ",router,"#$#")

print_test("Test #7: ",router,None)

print_test("Test #8: ",router,"#home/")

print_test("Test #9: ",router,"/home/products/1234/details")

print_test("Test #10: ",router,"/home/products/1234/details\asdcdsasdasd")







