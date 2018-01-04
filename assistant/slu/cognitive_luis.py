from luis_sdk import LUISClient

class CognitiveLuis():
    def __init__(self,appid,appkey):
        self.appid = appid
        self.appkey = appkey

        if self.appid == '':
            raise Exception('COGNITIVE_LUIS_APPID is empty')
        if self.appkey == '':
            raise Exception('COGNITIVE_LUIS_APPKEY is empty')

    def understand(self,text):
        client = LUISClient(self.appid, self.appkey, True)
        res = client.predict(text)
        top = res.get_top_intent()
        entities = res.get_entities()
        entities = [(x.get_type(), x.get_name()) for x in entities]
        intent = top.get_name()
        result = (intent, entities)
        return result
