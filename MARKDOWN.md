# Markdown để viết write-up

Mở file `.md` bằng VS Code. Trên Windows, dùng `Ctrl+Shift+V` để xem trước; dùng `Ctrl+K`, thả tay rồi nhấn `V` để mở cạnh cửa sổ soạn thảo.

| Muốn hiển thị | Cú pháp |
| --- | --- |
| Tiêu đề chính | `# Tên bài` |
| Mục lớn | `## Phân tích` |
| Mục con | `### Quan sát đầu tiên` |
| Chữ đậm | `**điểm quan trọng**` |
| Chữ nghiêng | `*giả thuyết*` |
| Mã trong dòng | Bao `solve.py` bằng một dấu backtick mỗi bên |
| Danh sách | `- Nội dung` |
| Danh sách đánh số | `1. Bước đầu` |
| Trích dẫn ngắn | `> Nội dung trích dẫn` |
| Liên kết | `[Tên hiển thị](https://example.com)` |
| Ảnh | `![Mô tả ảnh](images/01-observation.png)` |
| Việc chưa hoàn thành | `- [ ] Kiểm tra đường dẫn ảnh` |
| Việc đã hoàn thành | `- [x] Đọc lại kết luận` |

Để viết block code, đặt ba backtick trước và sau đoạn mã; thêm tên ngôn ngữ ở hàng mở đầu:

````markdown
```python
import base64

print(base64.b64decode("SGVsbG8=", validate=True).decode("utf-8"))
```

```text
Hello
```
````

Dùng `python` cho Python, `bash` cho Git Bash/Linux shell, `powershell` cho PowerShell, và `text` cho output. Thêm một dòng trống trước và sau block code, bảng hoặc danh sách.

Đường dẫn ảnh tính từ file Markdown chứa nó. Nếu bài là `ten-bai/README.md`, ảnh là `ten-bai/images/01-observation.png`, dùng `images/01-observation.png`. Không dùng đường dẫn `C:\Users\...` trong bài công khai. Tên file và chữ hoa/thường phải khớp.

Ví dụ bảng:

```markdown
| Dấu hiệu | Nhận định |
| --- | --- |
| Có ký tự `=` ở cuối | Có thể là Base64; cần kiểm tra thêm |
```

Nguồn: [GitHub Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax), [VS Code Markdown](https://code.visualstudio.com/docs/languages/markdown).
