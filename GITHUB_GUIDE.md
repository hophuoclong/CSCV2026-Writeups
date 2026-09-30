# Đưa bộ write-up lên GitHub

Các lệnh dưới đây dùng **Git Bash trên Windows**. Bộ file này chưa phải repository Git và chưa được đăng lên tài khoản GitHub nào.

## 1. Chuẩn bị

Cài [Git for Windows](https://git-scm.com/install/windows) và [VS Code](https://code.visualstudio.com/). Giải nén bộ file và mở đúng thư mục `ctf-writeups` có `README.md` bằng VS Code: **File → Open Folder**.

Trong VS Code: **Terminal → New Terminal**. Nếu terminal đang là PowerShell, chọn menu cạnh dấu `+`, chọn Git Bash. Hoặc mở Git Bash trực tiếp tại thư mục bằng menu chuột phải của Windows.

```bash
git --version
git config --global user.name "Long"
git config --global user.email "EMAIL_CUA_BAN"
```

Thay `EMAIL_CUA_BAN` trước khi chạy. Dùng email đã gắn với tài khoản GitHub hoặc sao chép địa chỉ `noreply` trong **GitHub → Settings → Emails**. `user.name` là tên tác giả commit, không phải thao tác đăng nhập. `--global` đặt giá trị mặc định cho các repository trên máy.

Nguồn: [Tên tác giả Git](https://docs.github.com/en/get-started/git-basics/setting-your-username-in-git), [Email commit](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

## 2. Tạo repository trống

1. Mở [GitHub New Repository](https://github.com/new), chọn tài khoản của bạn ở Owner.
2. Đặt tên `ctf-writeups` và nhập mô tả ngắn.
3. Chọn Public nếu muốn chia sẻ, hoặc Private nếu đang viết nháp.
4. Với cách đẩy thư mục có sẵn trong hướng dẫn này, để **Add README tắt**, `.gitignore` và License là **None**. File README và cấu hình bỏ qua đã có ở máy.
5. Bấm **Create repository** và sao chép URL HTTPS của repository.

Nguồn: [Đưa code có sẵn lên GitHub](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github).

## 3. Lần đẩy đầu tiên

Terminal phải đang ở thư mục `ctf-writeups`, không ở thư mục bao ngoài. Có thể kiểm tra bằng `pwd` và `ls`.

```bash
git init -b main
git status
git add .
git diff --cached --stat
git diff --cached
```

Xem danh sách và nội dung sắp đưa vào commit. Nếu Git mở trình xem nhiều trang, nhấn `q` để thoát. Khi đúng, chạy:

```bash
git commit -m "docs: start CTF writeup collection"
git remote add origin https://github.com/TEN_GITHUB/ctf-writeups.git
git remote -v
git push -u origin main
```

Thay `TEN_GITHUB` bằng username thật; URL phải khớp repository vừa tạo. `add` chọn thay đổi, `commit` lưu một mốc trên máy, `push` đưa các commit lên GitHub. `origin` là tên của địa chỉ remote; `main` là tên nhánh; `-u` ghi nhớ nhánh theo dõi cho những lần push sau.

Git for Windows có Git Credential Manager. Khi được yêu cầu xác thực, đăng nhập GitHub qua cửa sổ trình duyệt và hoàn thành 2FA nếu có. Mật khẩu tài khoản GitHub không dùng làm mật khẩu Git qua HTTPS. Nếu Git yêu cầu nhập mật khẩu tại terminal, dùng cơ chế token được GitHub hỗ trợ hoặc cài/cấu hình lại GCM; không nhúng token vào URL remote.

Nguồn: [Git Credential Manager](https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git), [Xác thực GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github).

## 4. Mỗi lần thêm hoặc sửa bài

Trước khi sửa, khi `git status` báo working tree sạch:

```bash
git pull --ff-only
```

Sau khi sửa và lưu các file:

```bash
git status
git diff
git add .
git diff --cached --stat
git diff --cached
git commit -m "docs: add writeup for ten-bai"
git push
```

`git diff` trước khi add không hiển thị nội dung file mới chưa được theo dõi; bước xem diff sau khi add giúp kiểm tra cả những file đó. Thay nội dung commit theo thay đổi thực tế, chẳng hạn `docs: explain base64 validation` hoặc `docs: fix image path`.

Nguồn: [Thêm file bằng Git](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository), [git pull](https://git-scm.com/docs/git-pull).

## 5. Cách dùng giao diện web

Nếu chọn cách này ngay từ đầu, có thể bật **Add README** khi tạo kho. Khi kho đã có README: chọn **Add file → Upload files**, kéo các file/thư mục bên trong `ctf-writeups` lên và giữ nguyên cấu trúc. Không chỉ tải ZIP lên nếu muốn GitHub hiển thị bài Markdown trực tiếp. Đọc danh sách file, nhập mô tả commit rồi commit vào `main` nếu kho cá nhân cho phép; nếu chọn nhánh mới, tạo pull request để đưa thay đổi vào `main`.

Để viết ngay trên GitHub: **Add file → Create new file**, nhập tên dạng `2026/ten-giai/misc/ten-bai/README.md`, dán Markdown, chọn **Preview**, rồi **Commit changes**. Để sửa bài đã có, mở file và bấm biểu tượng bút chì.

Nếu sau đó chuyển sang dùng Git, hãy `git clone` kho đã có thay vì tạo một lịch sử Git độc lập:

```bash
git clone https://github.com/TEN_GITHUB/ctf-writeups.git
cd ctf-writeups
```

Thực hiện trong một thư mục cha chưa có thư mục con cùng tên.

Nguồn: [Tạo repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories), [Thêm file](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository).

## 6. Khi gặp lỗi

| Thông báo | Cách xử lý |
| --- | --- |
| `git` không được nhận diện | Cài Git, đóng rồi mở lại terminal/VS Code. |
| `Author identity unknown` | Cấu hình lại `user.name` và `user.email`. |
| `src refspec main does not match any` | Kiểm tra đã có commit bằng `git log -1` và tên nhánh bằng `git branch --show-current`. |
| `remote origin already exists` | Xem `git remote -v`; nếu URL sai, dùng `git remote set-url origin URL_DUNG`. |
| `non-fast-forward` | Remote có thay đổi chưa hợp nhất; xem hướng dẫn ngay dưới bảng. |
| `nothing to commit` | Lưu file, kiểm tra `pwd`, `git status` và file có bị bỏ qua hay không. Nếu không có thay đổi thì không cần commit mới. |
| Ảnh không hiện | Kiểm tra file đã được đưa lên, đường dẫn tương đối và chữ hoa/thường. |

Nếu hai bên có chung lịch sử nhưng cùng có commit mới, với working tree sạch và commit local chưa từng được push, có thể chạy `git pull --rebase origin main`, giải quyết xung đột nếu có, rồi `git push`. Nếu cần hủy lần rebase đang dở, dùng `git rebase --abort`.

Nếu kho web đã được tạo với README còn bạn tự `git init` thư mục riêng, cách dễ hiểu là clone kho web sang một thư mục mới rồi chép file bài viết vào đó, bỏ qua thư mục `.git` của bản cũ. Không dùng force push để xử lý nhầm tình huống này.

## 7. File lớn và thông tin riêng

GitHub giới hạn mỗi file tải bằng web ở 25 MiB; Git thường chặn file lớn hơn 100 MiB. Với memory dump/PCAP lớn, ghi nguồn tải và checksum trong bài; cân nhắc Git LFS nếu cần lưu chúng cùng dự án.

File `.gitignore` đi kèm bỏ qua môi trường Python, cache, `.env`, khóa riêng theo tên thông dụng, thư mục `private/` và `raw-large/`. Nó không tự xóa file từng được commit, không lọc nội dung ảnh/log, và không thay thế việc xem diff trước khi công khai. Trong cách tải bằng web, bạn vẫn phải tự chọn đúng file cần đăng.

Nguồn: [Giới hạn tệp GitHub](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository), [gitignore](https://git-scm.com/docs/gitignore).
