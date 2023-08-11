from model.group import Group
import random
import allure


def test_modify_group_name(app, db, check_ui):
    with allure.step('Given a non-empty group list'):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="Test"))
        old_groups = db.get_group_list()
    with allure.step('Given a random group from the list'):
        group = random.choice(old_groups)
    modified_group = Group(name="New group", id=group.id)
    with allure.step('When I modify a group %s from the list' % group):
        app.group.modify_group_by_id(group.id, modified_group)
    with allure.step('Then the new group list is equal to the old group list with the modified group'):
        new_groups = db.get_group_list()
        assert len(old_groups) == len(new_groups)
        for i, g in enumerate(old_groups):
            if g.id == group.id:
                old_groups[i] = modified_group
                break
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
