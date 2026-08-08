# # # # 

# # # import logging

# # # logging.basicConfig(

# # #     level=logging.INFO,

# # #     format="%(name)s - %(levelname)s - %(message)s"

# # # )

# # # auth_logger = logging.getLogger("Authentication")

# # # db_logger = logging.getLogger("Database")

# # # ai_logger = logging.getLogger("AI")

# # # auth_logger.warning("Login Failed")

# # # db_logger.info("Connected")

# # # ai_logger.info("Generating Response")


# # # pattern 1 logging exceptions 

# # import logging

# # logging.basicConfig(
# #     level=logging.INFO,
# #     format="%(asctime)s - %(levelname)s - %(message)s"
# # )

# # try:

# #     result = 10 / 0

# # except Exception:

# #     logging.exception("Unexpected Error")



# import logging
# import time

# logging.basicConfig(level=logging.INFO)

# def process():

#     start = time.time()

#     time.sleep(2)

#     end = time.time()

#     logging.info(f"Execution Time: {end-start:.2f} seconds")

# process()


# import logging

# logging.basicConfig(level=logging.INFO)

# prompt = "Explain Machine Learning"

# logging.info(f"Prompt Received: {prompt}")
import logging
import time

logging.basicConfig(

    level=logging.INFO,

    format="%(asctime)s - %(levelname)s - %(message)s"

)

logging.info("Application Started")

prompt = "Explain Deep Learning"

logging.info(f"Prompt Received: {prompt}")

start = time.time()

time.sleep(2)

logging.info("Generating Response")

end = time.time()

logging.info(f"Execution Time: {end-start:.2f} seconds")

logging.info("Response Delivered")


