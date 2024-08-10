# import qrcode
# import random
# import string
# import os

# class QRAttendanceSystem:
#     def __init__(self):
#         self.students = {}

#     def generate_qr_code(self, student_id):
#         qr = qrcode.QRCode(
#             version=1,
#             error_correction=qrcode.constants.ERROR_CORRECT_L,
#             box_size=10,
#             border=4,
#         )
#         qr.add_data(student_id)
#         qr.make(fit=True)

#         img = qr.make_image(fill_color="black", back_color="white")
#         img_file = f"{student_id}.png"
#         img.save(img_file)
#         img.show()  # Display the QR code image

#     def generate_student_id(self):
#         return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

#     def register_student(self, name):
#         student_id = self.generate_student_id()
#         self.students[student_id] = name
#         self.generate_qr_code(student_id)
#         return student_id

#     def scan_qr_code(self, qr_code):
#         if qr_code in self.students:
#             return self.students[qr_code]
#         else:
#             return "Invalid QR Code"

# # Example Usage
# attendance_system = QRAttendanceSystem()

# # Registering students
# student1_id = attendance_system.register_student("John Doe")
# student2_id = attendance_system.register_student("Jane Smith")

# # Scanning QR Codes
# print(attendance_system.scan_qr_code(student1_id))  # Output: John Doe
# print(attendance_system.scan_qr_code(student2_id))  # Output: Invalid QR Code

import qrcode
import random
import string
import os

class QRAttendanceSystem:
    def __init__(self):
        self.students = {}

    def generate_qr_code(self, student_id):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(student_id)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img_file = f"{student_id}.png"
        img.save(img_file)  # Save the QR code image with student's ID as filename
        img.show()  # Display the QR code image

    def generate_student_id(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    def register_student(self, name):
        student_id = self.generate_student_id()
        self.students[student_id] = name
        self.generate_qr_code(student_id)
        return student_id

    def scan_qr_code(self, qr_code):
        if qr_code in self.students:
            return self.students[qr_code]
        else:
            return "Invalid QR Code"

# Example Usage
attendance_system = QRAttendanceSystem()

# Registering students
student1_id = attendance_system.register_student("John Doe")
student2_id = attendance_system.register_student("Jane Smith")

# Scanning QR Codes
print(attendance_system.scan_qr_code(student1_id))  # Output: John Doe
print(attendance_system.scan_qr_code(student2_id))  # Output: Invalid QR Code
