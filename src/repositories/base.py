from sqlalchemy import insert, select, delete, update

class BaseRepository :
    model = None 
    schema = None
    
    def __init__(self, session) :
        self.session = session
    
    async def add(self, **data) :
        add_user_stmt = insert(self.model).values(**data)
        await self.session.execute(add_user_stmt)
    
    async def get_all(self) : 
        query = select(self.model)
        
        result = await self.session.execute(query) 
        
        return [self.schema.model_validate(model, from_attributes=True) for model in result.scalars.all()]
    
    async def get_one_or_none(self, **filter_by) :
        query = select(self.model).filter_by(**filter_by)
        
        result = await self.session.execute(query)
        
        model = result.scalars().one_or_none()
        
        if model is None :
            return None
        
        return self.schema.model_validate(model, from_attributes=True) 
    
    async def edit(self, data, is_patch=False, **filter_by) :
        edit_hotel_stmt = (update(self.model).filter_by(**filter_by).
        values(**data.model_dump(exclude_unset=is_patch)))
        await self.session.execute(edit_hotel_stmt)
        
    async def delete(self, **filter_by) :
        delete_stmt = delete(self.model).filter_by(**filter_by)
        await self.session.execute(delete_stmt)
