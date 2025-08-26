from fastapi import APIRouter

shop = APIRouter()


@shop.get('/bed')
async def get_bed():
    return {'shop': 'bed'}


@shop.get('/food')
async def get_food():
    return {'shop': 'food'}
