import asyncio

async def count():
	print("one")
	await asyncio.sleep(1)
	print("two")

async def func():
	count()
	count()
	count()

func()