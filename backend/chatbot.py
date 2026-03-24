import google.generativeai as genai
import os
import json


class GeminiBot:
    def __init__(self, api_key):
        self.api_key = api_key
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def generate_response(self, query, context_chunks):
        """
        Generate a response using Gemini based on the query and retrieved context.
        """
        # Ghi log cấu trúc của context_chunks

        # Sử dụng thuộc tính page_content thay vì text
        context_text = "\n\n".join([doc.page_content for doc in context_chunks if hasattr(doc, 'page_content')])
        system_prompt = f"""Bạn là một trợ lý tư vấn pháp luật thông minh và chuyên nghiệp.
        Hãy dựa vào câu hỏi người dùng và các thông tin ngữ cảnh được cung cấp để đưa ra câu trả lời chính xác và hữu ích nhất, luôn hiển thị các thông tin mới nhất lên trước các thông tin cũ.
        Câu trả lời bạn đưa ra phải chuyên nghiệp, không được máy móc, cảm xúc và thân thiện với người dùng, theo phong cách của một luật sư tư vấn pháp luật chuyên nghiệp tại Việt Nam.
        Khi trích dẫn thông tin từ tài liệu, hãy cung cấp tên luật, nghị quyết, điều mấy,... và kèm theo thời gian ban hành và hiệu lực
        Nếu câu hỏi không liên quan đến pháp luật, hãy lịch sự từ chối trả lời.

        Ngữ cảnh:
        {context_text}

        Câu hỏi: {query}

        Trả lời:"""

        try:
            response = self.model.generate_content(system_prompt)

            # Ghi log nội dung của response.text
            # print("Raw response from Gemini API:", response.text)



            # Nếu không phải hợp đồng, trả về văn bản
            return response.text
        except Exception as e:
            return json.dumps({"response": f"Xin lỗi, đã xảy ra lỗi khi gọi API Gemini: {str(e)}"}, ensure_ascii=False)
        