

class CreateResponse(BaseResponse):
	owner_id = None
	card_id = None

class DeleteResponse(BaseResponse):
	owner_id = None
	card_id = None
	error = None

class EditResponse(BaseResponse):
	owner_id = None
	card_id = None

class GetByIdResponse(BaseResponse):
	

class GetUploadURLResponse(BaseResponse):
	

class GetResponse(BaseResponse):
	count = None
	items = None