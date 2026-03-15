import sys

file_path = 'c:/xampp/htdocs/dentconsent/webapp/register.html'
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
except Exception as e:
    print('Error reading', e)
    sys.exit(1)

replacements = [
    (
'''                                <label class="form-label">FULL NAME</label>
                                <div class="input-wrapper">
                                    <span class="material-icons input-icon">person</span>
                                    <input type="text" name="p_full_name" class="form-control" placeholder="Jane Doe">
                                </div>''',
'''                                <label class="form-label" style="display: flex; align-items: center; gap: 6px;"><span class="material-icons" style="font-size: 18px;">person</span> FULL NAME</label>
                                <input type="text" name="p_full_name" class="form-control" placeholder="Jane Doe">'''
    ),
    (
'''                                <label class="form-label">MOBILE NUMBER</label>
                                <div class="input-wrapper">
                                    <span class="material-icons input-icon">phone</span>
                                    <input type="tel" name="p_mobile_number" class="form-control"
                                        placeholder="1234567890" maxlength="10">
                                </div>''',
'''                                <label class="form-label" style="display: flex; align-items: center; gap: 6px;"><span class="material-icons" style="font-size: 18px;">phone</span> MOBILE NUMBER</label>
                                <input type="tel" name="p_mobile_number" class="form-control"
                                        placeholder="1234567890" maxlength="10">'''
    ),
    (
'''                                <label class="form-label">EMAIL ADDRESS</label>
                                <div class="input-wrapper">
                                    <span class="material-icons input-icon">mail</span>
                                    <input type="email" name="p_email" class="form-control"
                                        placeholder="jane@example.com">
                                </div>''',
'''                                <label class="form-label" style="display: flex; align-items: center; gap: 6px;"><span class="material-icons" style="font-size: 18px;">mail</span> EMAIL ADDRESS</label>
                                <input type="email" name="p_email" class="form-control"
                                        placeholder="jane@example.com">'''
    ),
    (
'''                                    <label class="form-label">DATE OF BIRTH</label>
                                    <div class="input-wrapper">
                                        <span class="material-icons input-icon">calendar_today</span>
                                        <input type="text" name="p_dob" class="form-control" placeholder="DD-MM-YYYY">
                                    </div>''',
'''                                    <label class="form-label" style="display: flex; align-items: center; gap: 6px;"><span class="material-icons" style="font-size: 18px;">calendar_today</span> DATE OF BIRTH</label>
                                    <input type="text" name="p_dob" class="form-control dob-input" placeholder="dd-mm-yyyy" maxlength="10">'''
    ),
    (
'''                                    <label class="form-label">GENDER</label>
                                    <div class="input-wrapper">
                                        <select name="p_gender" class="form-control" style="padding-left: 1rem;">
                                            <option value="" disabled selected>Select</option>
                                            <option value="Male">Male</option>
                                            <option value="Female">Female</option>
                                            <option value="Other">Other</option>
                                        </select>
                                    </div>''',
'''                                    <label class="form-label">GENDER</label>
                                    <select name="p_gender" class="form-control">
                                        <option value="" disabled selected>Select</option>
                                        <option value="Male">Male</option>
                                        <option value="Female">Female</option>
                                        <option value="Other">Other</option>
                                    </select>'''
    ),
    (
'''                                <label class="form-label">ALLERGIES</label>
                                <div class="input-wrapper">
                                    <span class="material-icons input-icon">medical_services</span>
                                    <input type="text" name="p_allergies" class="form-control"
                                        placeholder="e.g. Penicillin, Peanuts">
                                </div>''',
'''                                <label class="form-label" style="display: flex; align-items: center; gap: 6px;"><span class="material-icons" style="font-size: 18px;">medical_services</span> ALLERGIES</label>
                                <input type="text" name="p_allergies" class="form-control"
                                        placeholder="e.g. Penicillin, Peanuts">'''
    ),
    (
'''                                <label class="form-label">HOME ADDRESS</label>
                                <div class="input-wrapper">
                                    <span class="material-icons input-icon">home</span>
                                    <input type="text" name="p_residential_address" class="form-control"
                                        placeholder="Street, House No, Landmark">
                                </div>''',
'''                                <label class="form-label" style="display: flex; align-items: center; gap: 6px;"><span class="material-icons" style="font-size: 18px;">home</span> HOME ADDRESS</label>
                                <input type="text" name="p_residential_address" class="form-control"
                                        placeholder="Street, House No, Landmark">'''
    ),
    (
'''                                <label class="form-label">PASSWORD</label>
                                <div class="input-wrapper">
                                    <span class="material-icons input-icon">lock</span>
                                    <input type="password" name="p_password" class="form-control"
                                        placeholder="••••••••">
                                </div>''',
'''                                <label class="form-label" style="display: flex; align-items: center; gap: 6px;"><span class="material-icons" style="font-size: 18px;">lock</span> PASSWORD</label>
                                <input type="password" name="p_password" class="form-control"
                                        placeholder="••••••••">'''
    ),
    (
'''                                <label class="form-label">CONFIRM PASSWORD</label>
                                <div class="input-wrapper">
                                    <span class="material-icons input-icon">lock</span>
                                    <input type="password" name="p_confirm_password" class="form-control"
                                        placeholder="••••••••">
                                </div>''',
'''                                <label class="form-label" style="display: flex; align-items: center; gap: 6px;"><span class="material-icons" style="font-size: 18px;">lock</span> CONFIRM PASSWORD</label>
                                <input type="password" name="p_confirm_password" class="form-control"
                                        placeholder="••••••••">'''
    ),
    (
'''                                <label class="form-label">FULL NAME</label>
                                <div class="input-wrapper">
                                    <span class="material-icons input-icon">person</span>
                                    <input type="text" name="d_full_name" class="form-control"
                                        placeholder="Dr. Jane Doe">
                                </div>''',
'''                                <label class="form-label" style="display: flex; align-items: center; gap: 6px;"><span class="material-icons" style="font-size: 18px;">person</span> FULL NAME</label>
                                <input type="text" name="d_full_name" class="form-control"
                                        placeholder="Dr. Jane Doe">'''
    ),
    (
'''                                <label class="form-label">MOBILE NUMBER</label>
                                <div class="input-wrapper">
                                    <span class="material-icons input-icon">phone</span>
                                    <input type="tel" name="d_mobile_number" class="form-control"
                                        placeholder="1234567890" maxlength="10">
                                </div>''',
'''                                <label class="form-label" style="display: flex; align-items: center; gap: 6px;"><span class="material-icons" style="font-size: 18px;">phone</span> MOBILE NUMBER</label>
                                <input type="tel" name="d_mobile_number" class="form-control"
                                        placeholder="1234567890" maxlength="10">'''
    ),
    (
'''                                <label class="form-label">EMAIL ADDRESS</label>
                                <div class="input-wrapper">
                                    <span class="material-icons input-icon">mail</span>
                                    <input type="email" name="d_email" class="form-control"
                                        placeholder="doctor@clinic.com">
                                </div>''',
'''                                <label class="form-label" style="display: flex; align-items: center; gap: 6px;"><span class="material-icons" style="font-size: 18px;">mail</span> EMAIL ADDRESS</label>
                                <input type="email" name="d_email" class="form-control"
                                        placeholder="doctor@clinic.com">'''
    ),
    (
'''                                    <label class="form-label">DATE OF BIRTH</label>
                                    <div class="input-wrapper">
                                        <span class="material-icons input-icon">calendar_today</span>
                                        <input type="text" name="d_dob" class="form-control" placeholder="DD-MM-YYYY">
                                    </div>''',
'''                                    <label class="form-label" style="display: flex; align-items: center; gap: 6px;"><span class="material-icons" style="font-size: 18px;">calendar_today</span> DATE OF BIRTH</label>
                                    <input type="text" name="d_dob" class="form-control dob-input" placeholder="dd-mm-yyyy" maxlength="10">'''
    ),
    (
'''                                    <label class="form-label">GENDER</label>
                                    <div class="input-wrapper">
                                        <select name="d_gender" class="form-control" style="padding-left: 1rem;">
                                            <option value="" disabled selected>Select</option>
                                            <option value="Male">Male</option>
                                            <option value="Female">Female</option>
                                            <option value="Other">Other</option>
                                        </select>
                                    </div>''',
'''                                    <label class="form-label">GENDER</label>
                                    <select name="d_gender" class="form-control">
                                        <option value="" disabled selected>Select</option>
                                        <option value="Male">Male</option>
                                        <option value="Female">Female</option>
                                        <option value="Other">Other</option>
                                    </select>'''
    ),
    (
'''                                <label class="form-label">DENTAL COUNCIL ID</label>
                                <div class="input-wrapper">
                                    <span class="material-icons input-icon">badge</span>
                                    <input type="text" name="d_council_id" class="form-control"
                                        placeholder="e.g. MH/12345">
                                </div>''',
'''                                <label class="form-label" style="display: flex; align-items: center; gap: 6px;"><span class="material-icons" style="font-size: 18px;">badge</span> DENTAL COUNCIL ID</label>
                                <input type="text" name="d_council_id" class="form-control"
                                        placeholder="e.g. MH/12345">'''
    ),
    (
'''                                <label class="form-label">SPECIALIZATION</label>
                                <select name="d_specialization" class="form-control" style="padding-left: 1rem;">
                                    <option value="" disabled selected>Select</option>
                                    <option value="Implantologist">Implantologist</option>
                                    <option value="Prosthodontist">Prosthodontist</option>
                                    <option value="General Dentist">General Dentist</option>
                                    <option value="Orthodontist">Orthodontist</option>
                                </select>''',
'''                                <label class="form-label">SPECIALIZATION</label>
                                <select name="d_specialization" class="form-control">
                                    <option value="" disabled selected>Select</option>
                                    <option value="Implantologist">Implantologist</option>
                                    <option value="Prosthodontist">Prosthodontist</option>
                                    <option value="Orthodontist">Orthodontist</option>
                                </select>'''
    ),
    (
'''                                <label class="form-label">YEARS OF EXPERIENCE</label>
                                <div class="input-wrapper">
                                    <span class="material-icons input-icon">work</span>
                                    <input type="number" name="d_experience_years" class="form-control"
                                        placeholder="e.g. 5" min="0">
                                </div>''',
'''                                <label class="form-label" style="display: flex; align-items: center; gap: 6px;"><span class="material-icons" style="font-size: 18px;">work</span> YEARS OF EXPERIENCE</label>
                                <input type="number" name="d_experience_years" class="form-control"
                                        placeholder="e.g. 5" min="0">'''
    ),
    (
'''                                <label class="form-label">PASSWORD</label>
                                <div class="input-wrapper">
                                    <span class="material-icons input-icon">lock</span>
                                    <input type="password" name="d_password" class="form-control"
                                        placeholder="••••••••">
                                </div>''',
'''                                <label class="form-label" style="display: flex; align-items: center; gap: 6px;"><span class="material-icons" style="font-size: 18px;">lock</span> PASSWORD</label>
                                <input type="password" name="d_password" class="form-control"
                                        placeholder="••••••••">'''
    ),
    (
'''                                <label class="form-label">CONFIRM PASSWORD</label>
                                <div class="input-wrapper">
                                    <span class="material-icons input-icon">lock</span>
                                    <input type="password" name="d_confirm_password" class="form-control"
                                        placeholder="••••••••">
                                </div>''',
'''                                <label class="form-label" style="display: flex; align-items: center; gap: 6px;"><span class="material-icons" style="font-size: 18px;">lock</span> CONFIRM PASSWORD</label>
                                <input type="password" name="d_confirm_password" class="form-control"
                                        placeholder="••••••••">'''
    ),
    (
'''        // Initialize the default wizard on load
        setRole(currentRole, true);
    </script>''',
'''        // Auto-format DOB inputs
        document.querySelectorAll('.dob-input').forEach(input => {
            input.addEventListener('input', function(e) {
                if (e.inputType === 'deleteContentBackward') return;
                
                let v = this.value.replace(/\D/g, '');
                if (v.length >= 2 && v.length < 4) {
                    this.value = v.substring(0, 2) + '-' + v.substring(2);
                } else if (v.length >= 4) {
                    this.value = v.substring(0, 2) + '-' + v.substring(2, 4) + '-' + v.substring(4, 8);
                }
            });
        });

        // Initialize the default wizard on load
        setRole(currentRole, true);
    </script>'''
    )
]

for idx, (old, new) in enumerate(replacements):
    if old not in text:
        print(f"Warning: Chunk {idx} not found")
    else:
        text = text.replace(old, new)
        print(f"Replaced Chunk {idx}")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Done.")
