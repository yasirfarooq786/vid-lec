import os
import re

def clean_filename(filename):
    """
    Clean filename by removing:
    - _trimmed
    - _1.5x
    - _trimmed_1.5x
    - _1.5x_trimmed
    - Duplicate patterns
    """
    # Split into name and extension
    if '.' in filename:
        name_parts = filename.rsplit('.', 1)
        name = name_parts[0]
        ext = '.' + name_parts[1]
    else:
        name = filename
        ext = ''
    
    # Remove _trimmed (any occurrence)
    name = re.sub(r'_trimmed', '', name)
    
    # Remove _1.5x (any occurrence)
    name = re.sub(r'_1[.]5x', '', name)
    
    # Remove remaining double underscores
    name = re.sub(r'__+', '_', name)
    
    # Remove trailing underscore
    name = name.rstrip('_')
    
    # Fix common typo: "Phyics" -> "Physics"
    name = name.replace('Phyics', 'Physics')
    
    # Ensure consistent spacing (underscores instead of spaces)
    name = name.replace(' ', '_')
    
    # Remove any remaining multiple underscores
    name = re.sub(r'_+', '_', name)
    
    return name + ext

def preview_changes():
    """Preview what will be renamed without actually doing it"""
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith(('.mp4', '.mp3', '.jpg', '.png'))]
    
    print("="*100)
    print("PREVIEW - Files that will be renamed:")
    print("="*100)
    print()
    
    changes = []
    for old_name in sorted(files):
        new_name = clean_filename(old_name)
        if new_name != old_name:
            changes.append((old_name, new_name))
            print(f"📹 {old_name}")
            print(f"   → {new_name}\n")
    
    print(f"\nTotal: {len(changes)} files will be renamed")
    return changes

def rename_files():
    """Actually rename the files"""
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith(('.mp4', '.mp3', '.jpg', '.png'))]
    
    renamed_count = 0
    skipped_count = 0
    errors = []
    
    print("="*100)
    print("RENAMING FILES...")
    print("="*100)
    print()
    
    for old_name in sorted(files):
        new_name = clean_filename(old_name)
        
        if new_name != old_name:
            # Check if new name already exists
            if os.path.exists(new_name):
                print(f"⚠️  SKIPPED: {old_name}")
                print(f"   → {new_name} already exists!\n")
                skipped_count += 1
            else:
                try:
                    os.rename(old_name, new_name)
                    print(f"✅ RENAMED: {old_name}")
                    print(f"        → {new_name}\n")
                    renamed_count += 1
                except Exception as e:
                    print(f"❌ ERROR: {old_name}")
                    print(f"   {str(e)}\n")
                    errors.append((old_name, str(e)))
        else:
            print(f"⏭️  SAME: {old_name}\n")
    
    print("="*100)
    print(f"SUMMARY: {renamed_count} renamed, {skipped_count} skipped, {len(errors)} errors")
    print("="*100)
    
    if errors:
        print("\nErrors encountered:")
        for old, err in errors:
            print(f"  - {old}: {err}")

if __name__ == "__main__":
    print("\n🔧 File Cleanup Tool - Removes '_trimmed', '_1.5x', etc.")
    print("="*100)
    print()
    
    # First preview
    changes = preview_changes()
    
    if changes:
        print("\n" + "="*100)
        response = input("Proceed with renaming? (yes/no): ").strip().lower()
        
        if response == 'yes' or response == 'y':
            rename_files()
            print("\n✅ Done!")
        else:
            print("\n❌ Operation cancelled.")
    else:
        print("\n📌 No files need renaming.")